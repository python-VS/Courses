import random

from db import DataBase


class StudentDBManager:
    def __init__(self, db_name):
        self.__db_name = db_name

    def create_table(self):
        db = DataBase(self.__db_name)
        db.create_table("""
        CREATE TABLE IF NOT EXISTS students 
        (
          id         INTEGER PRIMARY KEY AUTOINCREMENT, 
          first_name TEXT NOT NULL,
          last_name  TEXT NOT NULL,
          patronymic TEXT NOT NULL
        );
        """)

    def alter_table_add_email(self):
        db = DataBase(self.__db_name)
        db.alter_table("""
        ALTER TABLE students 
        ADD COLUMN email TEXT; 
        """)

    def alter_column_add_group(self):
        db = DataBase(self.__db_name)
        db.execute_script("""
        PRAGMA foreign_keys=off;
        BEGIN TRANSACTION;
        ALTER TABLE students RENAME TO students_old;

        CREATE TABLE IF NOT EXISTS students 
        (
          id         INTEGER PRIMARY KEY AUTOINCREMENT, 
          first_name TEXT NOT NULL,
          last_name  TEXT NOT NULL,
          patronymic TEXT NOT NULL,
          email      TEXT NULL,
          group_id   INTEGER NULL,
          CONSTRAINT fk_group_id
            FOREIGN KEY (group_id)
            REFERENCES groups(id)
        );
        INSERT INTO students(id, first_name, last_name, patronymic, email) 
        SELECT * FROM students_old;
        COMMIT;

        PRAGMA foreign_keys=on;
        """)

    def save_new(self, first_name, last_name, patronymic):
        db = DataBase(self.__db_name)
        db.create_table(f"""
        INSERT INTO students(first_name, last_name, patronymic) 
        VALUES('{first_name}', '{last_name}', '{patronymic}');
        """)

    def select_even_by_id(self):
        db = DataBase(self.__db_name)
        return db.select(f"""
        SELECT * FROM students
        WHERE id % 2 = 0;
        """)

    def select_email_duplicates(self):
        db = DataBase(self.__db_name)
        return db.select(f"""
        SELECT email, COUNT(email) FROM students
        GROUP BY email
        HAVING COUNT(email) > 1;
        """)

    def set_email(self, _id, email):
        db = DataBase(self.__db_name)
        return db.update(f"""
        UPDATE students 
        SET email = '{email}'
        WHERE id = {_id};
        """)

    def set_group(self, _id, group_id):
        db = DataBase(self.__db_name)
        return db.update(f"""
        UPDATE students 
        SET group_id = {group_id}
        WHERE id = {_id};
        """)


class Student:
    db_manager = StudentDBManager('example.db')

    def __init__(self, last_name, first_name, patronymic):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic

    @classmethod
    def create_table(cls):
        cls.db_manager.create_table()

    @classmethod
    def alter_table_add_email(cls):
        cls.db_manager.alter_table_add_email()

    @classmethod
    def set_random_email(cls, emails):
        random.shuffle(emails)
        for _id, email in enumerate(emails, start=1):
            cls.db_manager.set_email(_id, email)

    @classmethod
    def select_even_by_id(cls):
        return cls.db_manager.select_even_by_id()

    @classmethod
    def select_email_duplicates(cls):
        return cls.db_manager.select_email_duplicates()

    @classmethod
    def alter_column_add_group(cls):
        return cls.db_manager.alter_column_add_group()

    @classmethod
    def set_random_group(cls, groups):
        random.shuffle(groups)
        for _id, group in enumerate(groups, start=1):
            cls.db_manager.set_group(_id, group)

    def save_new(self):
        self.db_manager.save_new(
            self.first_name, self.last_name, self.patronymic,
        )