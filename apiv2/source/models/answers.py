from marshmallow import fields, Schema
import datetime
from . import ConnectDb
from ..app import bcrypt


class Answers(ConnectDb):
    '''
    Creates the answers table and define its functionality using routes
    '''

    def __init__(self, data):
        self.answer_id = data.get('answer_id')
        self.question_id = data.get('question_id')
        self.user_id = data.get('user_id')
        self.content = data.get('content')
        self.comments = data.get('comments')
        # Hashing the password
        self.password = self.__generate__hash(data.get('password'))

    def __generate__hash(self, password):  # Hash the password before storage
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")


    def save(self):
        ConnectDb.session.add(self)
        ConnectDb.session.commit()

    def delete(self):
        ConnectDb.session.delete(self)
        ConnectDb.session.commit()

    '''def update(self):
        for key, item in items():
            if key == password:
                self.password = self.__generate__hash(value)
                setattr(self,key, item)
         ConnectDb.commit()'''
    '''
    Define the functionality of the answers table
    '''
    def verify__hash(self, password):  # Validates the user during login
        return bcrypt.check_password_hash(self.password, password)

# Printable object for the class
    def __repr__(self):
        return '<id {}>'.format(self.answer_id)
