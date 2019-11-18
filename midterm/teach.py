"""
This is an example for my question.md on github :https://github.com/magmagcup/somequiz/blob/master/teach.py
My approach:
For this question I store the data as a string in a list, Reason?. It look less confuser than list in list!

# Tip of the day
If your input have fix value use it, like for example in this question
We know that first input MUST have length = 4
So we could use that value as one of the condition to check if the input is correct or not

Another approach #1:
1 string for all data.

Another approach #2:
Store data as list in list.

Another approach #3:
Oop

It have much more approach than what I have mention above so I encourage you to try thinking for other approach.
"""


def print_data(student):
    print(f"ID: {student[0:4]}")
    print(f"Name: {student[4:-4]}")
    print(f"Grade: {student[-4:]}")


def get_input():
    student_id = input("Last 4 digit: ")
    name = input("First name: ")
    grade = input("Grade: ")
    return student_id + name + grade


data = []
answer = 0
while answer != "Q":
    answer = input("Welcome to program((A)dd/(Q)uit/(P)rint")
    if answer == "A":
        data.append(get_input())
    elif answer == "P":
        for i in data:
            print_data(i)
