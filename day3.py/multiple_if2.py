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
    else:
        bill = 12
        print("You have to pay 12$ ")
    photo=eval(input("have you required photo "))
    if photo == True :
        bill+=3
        print(f"your final bill is {bill} ")
    else:
        print(f"your bill is {bill} ")
else:
    print("sorry you can not ride the rollercoaster. ")