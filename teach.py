def print_data(student):
    print(f"ID: {student[0:4]}")
    print(f"Name: {student[4:-4]}")
    print(f"Grade: {student[-4:]}")


def get_input():
    student_id = input("Last 4 digit: ")
    name = input("First name: ")
    grade = input("Grade: ")
    return student_id + name + grade


def check_input(data, info_type):
    pass

data = []
answer = 0
while answer != "Q":
    answer = input("Welcome to program((A)dd/(Q)uit/(P)rint")
    if answer == "A":
        data.append(get_input())
    elif answer == "P":
        for student in data:
            print_data(student)
