from app.lab import *
from app.data import students

GREEN = "\x1b[32m"
CLEAR = "\x1b[0m"

def run_problem_1():
   average = calculate_student_average(students, "Alice Johnson")
   print(f"{GREEN}==Problem 1=={CLEAR}\nAverage: {average}")

def run_problem_2():
   (lowest, highest) = lowest_highest_grade(students)
   print(f"{GREEN}==Problem 2=={CLEAR}\nLowest: {lowest}\nHighest: {highest}")

def run_problem_3():
   print(f"{GREEN}==Problem 3=={CLEAR}")
   print_feedback(students)

def run_problem_4():
   average = exam_average(students, "Math Test 1")
   print(f"{GREEN}==Problem 4=={CLEAR}\nAverage: {average}")

def run_bonus():
   print_report_card("Alice Johnson", students["Alice Johnson"])

def run_all():
   run_problem_1()
   print()
   run_problem_2()
   print()
   run_problem_3()
   print()
   run_problem_4()