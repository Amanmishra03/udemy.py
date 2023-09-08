import random
letter = input("enter the letter:" ).split(",")
# numbers = int(input("enter the numbers: ")).split(",")
# symbols = input("enter the symbol: ").split(",")
# print("Wlcome! to the pypassword generator: ")
# nr_letter = int("how many letter do you want ? \n ")
# nr_number = int("enter how many digit do you want ? \n ")
# nr_symbol = int("enter how many symbol do you want ? \n ")
length = len(letter)
letter_name = length
random_letter = random.randint(0,length+1)
letter_name = letter[random_letter]
print(letter_name)
numbers = random.randint(0,9)
print(numbers)