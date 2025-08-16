students = {"Alice": 85, "Bob": 92, "Charlie": 78}
def top_student(students):
    highest_graded_student = max(students, key=students.get)
    return highest_graded_student

print(top_student(students))