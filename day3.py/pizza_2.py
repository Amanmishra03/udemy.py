print("Welcome to the python pizza deliveries: ")
size = input("what size pizza do you want ? S, M, or L : ")
add_pepporoni = input("do you want pepporoni ? Yes, or No : ")
extra_cheese = input("do you want to add extra cheese Yes or No : ")
bill = 0
if size == "S":
    print("The price is 15$. ")
    bill = 15
elif size == "M":
    print("The price is 20$. ")
    bill = 20
else:
    print("The price is 25$. ")
if add_pepporoni == "Yes":
    if size == "S":
        bill+=2
    else:
        bill+=3
if extra_cheese == "Yes":
    bill+=1
    print(f"your total bill is {bill} ")
else:
    print(f"your total bill is {bill} ")