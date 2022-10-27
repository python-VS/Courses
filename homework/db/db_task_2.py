from student import Student


if __name__ == '__main__':
    Student.alter_table_add_email()
    emails = [
        'a@gamil.com',
        'a@gamil.com',
        'b@gamil.com',
        'b@gamil.com',
        'c@gamil.com',
        'd@gamil.com',
        'd@gamil.com',
        'e@gamil.com',
        'j@gamil.com',
        'l@gamil.com',
    ]

    Student.set_random_email(emails)
    print(Student.select_email_duplicates())
