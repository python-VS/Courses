import random

from group import Group
from student import Student


if __name__ == '__main__':
    Group.create_table()
    Student.alter_column_add_group()
    group_data_list = [
        '65001',
        '65002',
        '65003',
        '65004',
    ]
    groups = [Group(data) for data in group_data_list]
    for group in groups:
        group.save_new()

    groups_for_students = [random.randint(1, 3) for _id in range(10)]
    Student.set_random_group(groups_for_students)
    print(Group.select_group_without_students())
