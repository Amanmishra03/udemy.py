num=int(input("Enter the no: "))
count=0
for i in range (2,num):
    if num%i == 0:
        count=count+1
if count == 0:
        print("number is prime")
        print(count)
else:
        print("number is not prime")         


num=int(input("Enter the no: "))
count=0
for i in range (2, int(num/2)):
    if num%i == 0:
        count=count+1
if count == 0:
        print("number is prime")
        print(count)
else:
        print("number is not prime")         