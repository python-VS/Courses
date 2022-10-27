from student import Student

if __name__ == '__main__':
    Student.create_table()
    student_data_list = [
        'Мельникова Ксения Витальевна',
        'Иванова София Ивановна',
        'Буракшаева Юлия Сергеевна',
        'Фурсова Елизавета Владимировна',
        'Сапсай Иван Алексеевич',
        'Богословский Артем Михайлович',
        'Самбикина Юлия Владимировна',
        'Шпак Ангелина Эдуардовна',
        'Пименов Максим Евгеньевич',
        'Сигида Валерия Романовна',
    ]

    students = [Student(*data.split()) for data in student_data_list]
    for student in students:
        student.save_new()

    print(Student.select_even_by_id())