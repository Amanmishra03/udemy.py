weight= int(input("Enter your Weight in kg: "))
height= float(input("Enter your height in m: "))
bmi=weight/height**2
# bmi1=int(bmi)
if bmi < 18.5:
    print("You are UNDERWEIGHT. ")
elif bmi < 25:
    print("You are having NORMALWEIGHT. ")
elif bmi < 30:
    print("You are OVERWEIGHT. ")
elif bmi < 35:
    print("You are OBESE. ")
else :
    print("you are clinically obese. ")

print(bmi)
print("hemlo")
