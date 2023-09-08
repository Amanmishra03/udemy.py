print("welcome to the rollercoaster ride")
height=int(input("Enter your height in cm: "))
if height> 120:
    print("wow! you can ride the Rollercoaster")
    age=int(input("What is your age: "))
    if age <= 18:
        print("Please pay $7. ")
    else:
        print("Please pay $12. ")
else:
    print("sorry you can not ride on Rollercoaster")
