'''
Define creation and droping of the tables
'''
from source import CONNECT


class DatabaseTables():
    '''
    Class defines all the database interactions
    '''

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

        cursor = CONNECT.cursor()
        # Call to execution the tables that have been created
        cursor.execute(users)
        cursor.execute(questions)
        cursor.execute(answers)
        cursor.execute(votes)
        CONNECT.commit()

    def drop_tables(self):
        '''
        Clearing the entire database
        '''
        cursor = CONNECT.cursor()
        cursor.execute('DROP TABLE users, questions, answers,votes;')
        CONNECT.commit()
        cursor.close()

