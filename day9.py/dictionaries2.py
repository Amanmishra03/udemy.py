programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# 1. retrieve item from dicctionary ?
'''If we want to print some information from a dictionary then 
if we want to print the value of a key then we have to write the variable in print function 
and after variable we use square bracket and write key in sq. bracket  '''

# print(programming_dictionary["Bug"])

# 2. To Add the data in dictionary ?
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# 3. create an empty dictionary ?
empty_dictionary = {}

# 4. wipe an existing dictionary ?
# programming_dictionary = {}
# print(programming_dictionary)

# 5. Edit an item in a dictionary ?
programming_dictionary["Bug"] = "a moth in your computer "
# print(programming_dictionary)

# 6. Loop through a dictionary ?
for thing in programming_dictionary:
    print(thing)
# it only give the key not value until we write 
    print(programming_dictionary[thing])
