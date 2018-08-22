import psycopg2
from flask_bcrypt import Bcrypt


# Initialize the db
class ConnectDb:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname= 'apidb' user=''postgres' host='localhost' password = '' port = '5432'")
            self.connection.autocommit = True  # After the SQL is done running
            self.cursor = self.connection.cursor()
        except psycopg2.DatabaseError:
            return 'Could not connect to the database'

bcrypt = Bcrypt()





    def create_table(self):
        create = "CREATE TABLE pet (id serial PRIMARY KEY, name VARCHAR[100], age integer NOT NULL)"
        self.cursor.execute(create)

    def insert_new_record(self):
        new_rec = ['misa', '9']  # Using a tuple for insertion
        insertion = "INSERT INTO pet(name, age) VALUES ('"+new_rec[0]+"','"+new_rec[1]+"')"
        self.cursor.execute(insertion)

    def query_all(self):
        self.cursor.execute('SELECT * FROM answers')
        answer = self.cursor.fetchall()
        for answ in answer:
            return "each answer : {0}". format(answ)

    def update(self):
        updating = "UPDATE answers SET age = 10 WHERE id = 1"
        self.cursor.execute(updating)

    def delete_table(self):
        delete = "DROP TABLE answers"
        self.cursor.execute(delete)

if __name__ == '__main__':
    database_connection = ConnectDb()
    database_connection.create_table()
    database_connection.insert_new_record()  # Calling the function in main, only one method called at a time
    # Change the values and call the function numerous times to add new objects

'''con = cur = db = None


def connect():
    global con, cur, db
    try:
        con = psycopg2.connect(DATABASE=apidb, user=postgres)
        cur = con.cursor()
        db = cur.execute ()
    except psycopg2.DatabaseError:
        if con:
            con.rollback()


def get_db():
    if not (con and cur and db):
        return con, cur, db
        # return (con, cur,db)
    imports
    con, cur, db = this_file_name.get_db()
    def fctn:
        db("Sql code")
        con.commit()'''
