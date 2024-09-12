import os
import psycopg2

class redis_handler():
    def __init__(self):
        self.conn = None

class db_handler():

    def __init__(self):
        self.conn = None

    def connect(self, host, port):
        self.conn = psycopg2.connect(
                host=host,
                port=port,
                database="flask_db",
                user="nnag",
                password="password"
                )
        self.cur = self.conn.cursor()

    def create_table(self, table):
        self.cur.execute('DROP TABLE IF EXISTS users')
        self.cur.execute('CREATE TABLE users (ID serial PRIMARY KEY,'
                                        'uname varchar (150) NOT NULL,'
                                        'password varchar (150) NOT NULL,'
                                        'permission varchar (150) NOT NULL);'
                                        )
    def insert_user(self, name, password, permission):
        self.cur.execute('INSERT INTO users (uname, password, permission)'
                    'VALUES (%s, %s, %s)',
                    (name,
                     password,
                     permission)
                    )
        self.conn.commit()

    def get_all_user(self):
        self.cur.execute('SELECT * from users')
        data = self.cur.fetchall()

        return data

    def close(self):
        self.cur.close()
        self.conn.close()
                                
