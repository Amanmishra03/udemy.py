''' to calculate the maximum marks that a student get in his exam 
    without using max function we have to use for loop for that '''

student_score = input("Enter the score: ").split()
print(type(student_score))
for n in range (0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
# print(max(student_score))
# print(min(student_score))

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"the highest score in the class is: {highest_score} ")