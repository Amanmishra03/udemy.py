print(" welcome to the Rollercoaster. ")
height=int(input("Enter your height in cm: "))
if height > 120:
    print("you can ride roller coaster")
    age=int(input("Enter your age "))
    if age < 12:
        print("you have to pay 5$ ")
    elif age < 18:
        print("Youth ticket is 7$ ")
    else:
        print("You have to pay 12$ ")
    photo=eval(input("have you required photo "))
    print(type(photo))
    if (photo == True and age < 12):
         print ("you have charge 3$ more ",5+3)
    elif (photo == True and age < 18):
        print("you have charge 3$ more",7+3)
    elif (photo == True and age > 18):
        print("you have charge 3$ more",12+3)
    else:
        print("you have no charges ")
else:
    print("sorry you can not ride the rollercoaster. ")
