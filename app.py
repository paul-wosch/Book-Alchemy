"""Run the Flask app and provide routing."""
from flask import Flask, request, render_template, redirect, url_for, flash
from config import DB_FILE_PATH, FLASK_SECRET_KEY, STATIC_PATH, TEMPLATES_PATH
from data_models import db, Author, Book

app = Flask(__name__, static_folder=STATIC_PATH, template_folder=TEMPLATES_PATH)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{str(DB_FILE_PATH)}"
app.secret_key = FLASK_SECRET_KEY

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    """Render home page with all books."""
    books = Book.query.all()
    return render_template("home.html", books=books)


@app.route("/book/<int:book_id>")
def single_book(book_id):
    """Render page for a single book."""
    book = Book.query.get(book_id)
    if book is None:
        return "Book not found", 404
    return render_template('single_book.html', book=book)


@app.route("/add_author", methods=["GET", "POST"])
def add_author():
    """Add a new author."""
    if request.method == "POST":
        name = request.form["name"]
        birthdate = request.form["birthdate"]
        date_of_death = request.form.get("date_of_death")

        new_author = Author(name=name, birth_date=birthdate, date_of_death=date_of_death)
        db.session.add(new_author)
        db.session.commit()
        flash(f"Author '{new_author.name}' added successfully!", "success")
        return redirect(url_for("home"))

    return render_template("add_author.html")


@app.route("/author/<int:author_id>/update", methods=["GET", "POST"])
def update_author(author_id):
    """Update an existing author."""
    author = Author.query.get_or_404(author_id)

    if request.method == "POST":
        author.name = request.form["name"]
        author.birth_date = request.form.get("birthdate")
        author.date_of_death = request.form.get("date_of_death")

        db.session.commit()
        flash(f"Author '{author.name}' updated successfully!", "success")
        return redirect(url_for("home"))

    return render_template("update_author.html", author=author, subtitle="Update Author")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    """Add a new book."""
    if request.method == "POST":
        title = request.form["title"]
        isbn = request.form["isbn"]
        year = int(request.form["year"])
        author_id = int(request.form["author_id"])

        new_book = Book(title=title, isbn=isbn, publication_year=year, author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        flash(f"Book '{new_book.title}' added successfully!", "success")
        return redirect(url_for("single_book", book_id=new_book.book_id))

    authors = Author.query.all()
    return render_template("add_book.html", authors=authors)


@app.route("/book/<int:book_id>/update", methods=["GET", "POST"])
def update_book(book_id):
    """Update an existing book."""
    book = Book.query.get_or_404(book_id)

    if request.method == "POST":
        book.title = request.form["title"]
        book.isbn = request.form["isbn"]
        year_str = request.form.get("year")
        book.publication_year = int(year_str) if year_str else None
        author_id_str = request.form.get("author_id")
        book.author_id = int(author_id_str) if author_id_str else None

        db.session.commit()
        flash(f"Book '{book.title}' updated successfully!", "success")
        return redirect(url_for("single_book", book_id=book.book_id))

    authors = Author.query.all()
    return render_template("update_book.html", book=book, authors=authors, subtitle="Update Book")


@app.route("/book/<int:book_id>/delete", methods=["POST"])
def delete_book(book_id):
    """Delete a book."""
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash(f"Book '{book.title}' deleted successfully!", "success")
    return redirect(url_for("home"))



@app.route("/sort/<field>")
def sort_books(field):
    """Sort books by given field."""
    if field == "title":
        books = Book.query.order_by(Book.title).all()
    elif field == "author":
        books = Book.query.join(Author).order_by(Author.name).all()
    else:
        books = Book.query.all()
    return render_template("home.html", books=books)


@app.route("/search", methods=["GET"])
def search():
    """Search books by title."""
    term = request.args.get("q", "")
    books = Book.query.filter(Book.title.like(f"%{term}%")).all()
    return render_template("home.html", books=books)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)
