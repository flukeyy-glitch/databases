from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import EmailAddress

emails = EmailAddress(email="lukwil0810@gmail.com")

engine = create_engine('sqlite:///emails.db', echo=True)

with Session(engine) as sess:
    sess.add(emails)
