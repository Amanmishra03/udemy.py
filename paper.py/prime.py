# num = int(input("enter the number "))
# count = 0
# for i in range (2,num):
#     if num%i == 0:
#         count = count+1
# if count == 0:
#     print(f"the {num} is prime number ")
# else:
#     print(f"the {num} is not prime number ")



# num = int(input("enter the number "))
# is_prime = True
# for i in range (2,num):
#     if num % i == 0:
#         is_prime = False
# if is_prime:
#     print("the no. is prime ")
# else:
#     print("it is not prime ")



num = int(input("enter the number "))
prime = True
for i in range (2,num):
    if num % i == 0:
        prime = False
if prime:
    print("the no. is prime ")
else:
    print("it is not prime ")