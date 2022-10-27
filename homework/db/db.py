import sqlite3
from sqlite3 import Error


class DataBase:
    def __init__(self, name):
        self.__name = name
        self.__conn = self.create_connection()

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.__name)
            return conn
        except Error as e:
            print(e)

        return conn

    def select(self, sql):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)

            return cursor.fetchall()
        except Error as e:
            print(e)

    def __modify(self, sql):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            self.__conn.commit()
        except Error as e:
            print(e)

    def insert(self, sql):
        self.__modify(sql)

    def update(self, sql):
        self.__modify(sql)

    def delete(self, sql):
        self.__modify(sql)

    def create_table(self, sql):
        self.__modify(sql)

    def alter_table(self, sql):
        self.__modify(sql)

    def execute_script(self, sql):
        try:
            cursor = self.__conn.cursor()
            cursor.executescript(sql)
            self.__conn.commit()
        except Error as e:
            print(e)

    def __del__(self):
        self.__conn.close()