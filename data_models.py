"""Provide models for SQLAlchemy."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Author(db.Model):
    """Represent an author entity."""
    author_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String)
    date_of_death = db.Column(db.String)

    def __repr__(self):
        """Return debug representation of author."""
        return f"<Author {self.name}>"

    def __str__(self):
        """Return readable string for author."""
        if self.birth_date and self.date_of_death:
            return f"{self.name} ({self.birth_date} – {self.date_of_death})"
        if self.birth_date:
            return f"{self.name} (born {self.birth_date})"
        return self.name


class Book(db.Model):
    """Represent a book entity."""
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String, unique=True)
    title = db.Column(db.String, nullable=False)
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.author_id'))

    author = db.relationship('Author', backref='books')

    def __repr__(self):
        """Return debug representation of book."""
        return f"<Book {self.title}>"

    def __str__(self):
        """Return readable string for book."""
        return f"{self.title} ({self.publication_year})"
