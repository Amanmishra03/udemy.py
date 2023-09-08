from random import randint


'''random is used to write random value or random integer'''
random_integer=randint(1,20)
print(random_integer)
random_integer=randint(1,100)
print(random_integer)

number = randint(0,20)
print(number)

number = randint(0,20)
number = randint(0,50)
if number > 25:
    print("head")
else:
    print("tail")