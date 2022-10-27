from db import DataBase


class GroupDBManager:
    def __init__(self, db_name):
        self.__db_name = db_name

    def create_table(self):
        db = DataBase(self.__db_name)
        db.create_table("""
        CREATE TABLE IF NOT EXISTS groups
        (
          id   INTEGER PRIMARY KEY AUTOINCREMENT, 
          name TEXT NOT NULL
        );
        """)

    def save_new(self, name):
        db = DataBase(self.__db_name)
        db.insert(f"""
        INSERT INTO groups(name) 
        VALUES('{name}');
        """)

    def select_group_without_students(self):
        db = DataBase(self.__db_name)
        return db.select(f"""
        SELECT groups.id, groups.name FROM groups
        LEFT JOIN students
        ON groups.id = students.group_id
        WHERE students.group_id IS NULL;
        """)


class Group:
    db_manager = GroupDBManager('example.db')

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_table(cls):
        cls.db_manager.create_table()

    @classmethod
    def select_group_without_students(cls):
        return cls.db_manager.select_group_without_students()

    def save_new(self):
        self.db_manager.save_new(self.name)