from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import EmailAddress


class Controller:
    def __init__(self):
        self.engine = create_engine('sqlite:///emails.db', echo=True)

    def save(self, email):
        """
        Save the email

        :param email:
        :return:
        """
        try:

            # save the model
            self.model.email = email
            self.model.save()

            with Session(self.engine) as sess:
                sess.add(self.model.email)
                sess.commit()

            # show a success message
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            raise ValueError(error)

