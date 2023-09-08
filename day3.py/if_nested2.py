print("Welcome to the Rollercoaster ")
height=int(input("Enter your height in cm: "))
if height > 120:
    print("wow! you can ride the Rollercoaster ")
    age=int(input("Enter your age: "))
    if age <= 12:
        print("please pay 5$. Thankyou. ")
    elif age <= 18:
        print("Please pay 7$. Thankyou. ")
    elif age <= 25:
        print("Please pay 12$. Thankyou. ")
    else:
        print("Please pay 15$ Thankyou. ")
else:
    print("Sorry you can not ride the Rollercoaster. ")