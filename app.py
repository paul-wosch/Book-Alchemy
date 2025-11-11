"""Run the Flask app and provide routing."""
from flask import Flask, request, render_template
from config import DB_FILE_PATH, STATIC_PATH, TEMPLATES_PATH
from data_models import db, Author, Book

app = Flask(__name__, static_folder=STATIC_PATH, template_folder=TEMPLATES_PATH)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{str(DB_FILE_PATH)}"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    books = Book.query.all()
    return render_template("home.html", books=books)


@app.route("/add_author", methods=["GET", "POST"])
def add_author():
    if request.method == "POST":
        name = request.form["name"]
        birthdate = request.form["birthdate"]
        date_of_death = request.form.get("date_of_death")

        new_author = Author(name=name, birth_date=birthdate, date_of_death=date_of_death)
        db.session.add(new_author)
        db.session.commit()
        return "Author added successfully!"

    return render_template("add_author.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        isbn = request.form["isbn"]
        year = int(request.form["year"])
        author_id = int(request.form["author_id"])

        new_book = Book(title=title, isbn=isbn, publication_year=year, author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        return "Book added successfully!"

    authors = Author.query.all()
    return render_template("add_book.html", authors=authors)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)