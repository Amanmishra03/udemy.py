'''Every Dictionary has two part  key point and its value . Dictionary is always written in {} where 
after key point we put a semicolon (:) and then its value each key have only one value '''
# syntex of dictionary
# {key: value}

# {"Bug": "An error in a program that prevent the program from running as expected."}

# for multiple value
# {"Bug": "An error in a program that prevent the program from running as expected.",
# "Function": "A piece of code that you can easily call over and over again.",
# "Loop": "The action of doing something over and over again." }

# for easy study we have write the code as written below
programming_dictionary = {
    "Bug": "An error in a program that prevent the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# 1.  to print a key we have to write as 
print(programming_dictionary["Function"])

# 2. to add some information in dictionary we have to write as
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# 3. wipe an exiting dictionary
programming_dictionary = {}
print(programming_dictionary)

# 4. Edit an item in a Dictionnary
programming_dictionary["Bug"] = "A moth in your computer "
print(programming_dictionary)







































