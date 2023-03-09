from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


# Base is called an Abstract Base Class - our SQL Alchemy models will inherit from this class
Base = declarative_base()

# Sets up a link table with book_id and author_id as foreign keys
# Base.metadata is a container object that keeps together many different features of the database
book_author = Table('book_author',
                    Base.metadata,
                    Column('author_id', Integer, ForeignKey("author.author_id")),
                    Column('book_id', Integer, ForeignKey('book.book_id')),
                    )


# Sets up a book table, this references the "author" and the "publisher" via the book_author and publisher tables

class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    publisher_id = Column(Integer, ForeignKey("publisher.publisher_id"))
    title = Column(String, nullable=False)
    isbn_number = Column(Integer, nullable=False)
    num_pages = Column(Integer, nullable=False)
    publication_date = Column(String, nullable=False)
    authors = relationship("Author",
                           secondary=book_author,
                           back_populates="books"
                           )


# Sets up an author table, this references the book via the book_author table

class Author(Base):
    __tablename__ = 'author'
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String, nullable=False)
    books = relationship("Book",
                         secondary=book_author,
                         back_populates="authors"
                         )


# Sets up a publisher table, this references the book via the foreign key publisher_id

class Publisher(Base):
    __tablename__ = 'publisher'
    publisher_id = Column(Integer, primary_key=True, autoincrement=True)
    publisher_name = Column(String, nullable=False)
