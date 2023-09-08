# prime number is a number which is only divisible by 1 and itself 
''' first mistake '''
# num = int(input("enter the number: "))
# for n in range (2,num):
#     if num % n == 0:
#         print("this is not prime no. ")
#     else:
#         print("this is a prime no. ")

''' correct way '''
# def prime_checker(number):
#     is_prime = True
#     for i in range(2,number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number. ")
#     else:
#         print("It's not a prime number. ")

# number = int(input("enter a number. "))
# prime_checker(number)

''' Not using def function '''
number = int(input("enter a number. "))
# here if we want to check the prime first we have to suppose it is a prime no.
is_prime = True
for i in range(2,number):
    if number % i == 0:
        is_prime = False
if is_prime:    
    print("It's a prime number. ")
else:
    print("It's not a prime number. ")
