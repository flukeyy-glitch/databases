from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Book, Author, Publisher

# Create some instances of the Author, Book and Publisher classes

authors = [Author(author_name="J.K. Rowling"), Author(author_name="Christopher Paolini"), Author(author_name="Jesus "
                                                                                                             "Christ"),
           Author(author_name="Philip Pullman"), Author(author_name="David Baddiel")]
publishers = [Publisher(publisher_name="Puffin"), Publisher(publisher_name="Oxford"), Publisher(publisher_name="Collins"
                                                                                                )]
books = [Book(title="Harry Potter and the Philosopher's Stone", isbn_number=102030405, num_pages=456,
              publication_date="02-12-34", publisher_id=1),
         Book(title="Harry Potter and the Goblet of Fire", isbn_number=102030406, num_pages=523,
              publication_date="05-12-34", publisher_id=1),
         Book(title="Harry Potter and the Prisoner of Azkaban", isbn_number=102030408, num_pages=443,
              publication_date="07-12-34", publisher_id=1),
         Book(title="The Bible", isbn_number=102650405, num_pages=456,
              publication_date="02-12-34", publisher_id=2),
         Book(title="Eragon", isbn_number=105030405, num_pages=606,
              publication_date="02-12-34", publisher_id=1),
         Book(title="Book of Dust", isbn_number=402030405, num_pages=906,
              publication_date="02-12-34", publisher_id=3)
         ]


# Connect to the activities database
engine = create_engine('sqlite:///books.db', echo=True)

# Create a session and add the people to the database
with Session(engine) as sess:
    sess.add_all(authors)
    sess.add_all(publishers)
    sess.add_all(books)
    sess.commit()
