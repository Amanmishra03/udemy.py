''' Write a program in which the no. divisible by 3 is print as fizz 
    the no. which is divisible by 5 is print as buzz
    if the no. is divisible by 3 and 5 both then it print fizzbuzz '''

for number in range (1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")    
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)