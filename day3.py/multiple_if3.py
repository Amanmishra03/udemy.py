print("Welcome to the Rollercoaster. ")
Height=eval(input("Enter your Height in cm. "))
bill=0
if Height > 120:
    print("wow! You can ride Rollercoaster. ")
    Age=int(input("Enter your age. "))
    if Age < 12:
        print("you have to pay 5$ ")
        bill = 5
    elif Age < 18:
        print("You have to pay 7$ ")
        bill = 7
    elif Age < 25:
        print("You have to pay 12$ ")
        bill = 12
    else:
        print("You have to pay 15$ ")
        bill = 15
    photo=input("Required photo Yes or No.")
    if photo == "Yes":
        bill+= 3
        print(f"your total bill is equal to {bill} ")
    else:
        print(f"Your total bill is equal to {bill} ")
else:
    print("Sorry you can't ride Rollercoaster. ")
