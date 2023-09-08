from unicodedata import name


# we can not concatenate strings to an integer
# for concatenate the sting to an integer we have to define data type
# after define the data type we can concatenate 
# num_char=(len(input("what is your name ")))
# new_num_char=str(num_char)
# print("your name has " + new_num_char + " characters")
# num_char=str(len(input("what is your name ")))
# print("your name has " + num_char + " characters")
print(70 + float("100.5"))
# in the above code we convert string(100.5) to float value to add
print(str(70) + str(90))
a=float(123)
print(type(a))
print(a)