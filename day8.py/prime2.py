# for checking of prime number
# number = int(input("Enter a number: "))
# is_prime = True
# for i in range(2,number):
#     if number % i == 0:
#         is_prime = False
# if is_prime == True:
#     print("It's a prime number. ")
# else:
#     print("It's not a prime number. ")
    
    
num = int(input("enter the number: "))
is_prime = True
for i in range (2,num):
    if num%i == 0:
        is_prime = False
if is_prime ==True:
    print("no. is prime. ")
else:
    print("no. is not prime")