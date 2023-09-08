'''calculate the average of student's height from a list of height '''

student_height = input["Enter the list of the student: "].split()
for n in range(0, len(student_height)):
    student_height = float(student_height)
print(student_height)
total_height = 0
for height in student_height:
    total_height += height
number_of_students = 0
for student in student_height:
    number_of_students += 1
average_height = round(total_height / number_of_students)
print(average_height)    


