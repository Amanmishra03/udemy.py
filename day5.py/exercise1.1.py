'''calculate the average of student's height from a list of height '''

student_height = input("enter the height of the students: ").split()
for n in range (0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)
total_height = 0
for height in student_height:
    total_height += height
print(total_height)
no_of_student = 0
for student in student_height:
    no_of_student += 1
print(no_of_student)
average_height = (total_height/no_of_student)
print(round(average_height))