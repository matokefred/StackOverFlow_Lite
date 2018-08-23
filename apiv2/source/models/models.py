'''
Define creation and droping of the tables
'''
from source.app import CONNECT


class DatabaseTables():
    '''
    Class defines all the database interactions
    '''
    def __init__(self):
        '''
        create the cursor object used by psycopg2 for database interaction
        '''
        self.cursor = CONNECT.cursor()

    def create_tables(self):
        '''
        Create all the relevant tables
        '''
        users = 'CREATE TABLE IF NOT EXISTS users(' \
                'id SERIAL PRIMARY KEY,' \
                'username varchar (50) NOT NULL,' \
                'email varchar (50) UNIQUE NOT NULL,' \
                'password VARCHAR (256) NOT NULL' \
                ');'

        questions = 'CREATE TABLE IF NOT EXISTS questions(' \
                    'questionId SERIAL PRIMARY KEY,' \
                    'userId INT NOT NULL REFERENCES users(id),' \
                    'body TEXT NOT NULL);'

        answers = 'CREATE TABLE IF NOT EXISTS answers(' \
                  'answerId SERIAL PRIMARY KEY,' \
                  'questionId INT NOT NULL REFERENCES questions(questionId),' \
                  'userId INT NOT NULL REFERENCES users(id),' \
                  'answer TEXT NOT NULL ,' \
                  'upvotes INT DEFAULT 0,' \
                  'downvotes INT DEFAULT 0,' \
                  'state BOOLEAN DEFAULT FALSE' \
                  'comments TEXT NOT NULL' \
                  ');'

        votes = 'CREATE TABLE IF NOT EXISTS votes(' \
                'voteId SERIAL REFERENCES answers(answerId),' \
                'voter INT NOT NULL REFERENCES users(id)' \
                ');'

        # Call to execution the tables that have been created
        self.cursor.execute(users)
        self.cursor.execute(questions)
        self.cursor.execute(answers)
        self.cursor.execute(votes)
        CONNECT.commit()

    def drop_tables(self):
        '''
        Clearing the entire database
        '''
        self.cursor = CONNECT.cursor()
        self.cursor.execute('DROP TABLE users, questions, answers,votes;')
        CONNECT.commit()

