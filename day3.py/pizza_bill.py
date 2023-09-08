print(" welcome to the Rollercoaster. ")
height=int(input("Enter your height in cm: "))
bill = 0
if height > 120:
    print("you can ride roller coaster")
    age=int(input("Enter your age "))
    if age < 12:
        bill=5
        print("you have to pay 5$ ")
    elif age < 18:
        bill = 7
        print("Youth ticket is 7$ ")
    elif age >= 45 and age <= 55:
        print("you can take free ride: ")
    else:
        bill = 12
        print("You have to pay 12$ ")
    photo=input("have you required photo Yes or No : ")
    if photo == "Yes":
        bill+=3
        print(f"your final bill is {bill} ")
    else:
        print(f"your bill is {bill} ")
else:
    print("sorry you can not ride the rollercoaster. ")