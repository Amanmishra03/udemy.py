import random
# name_of_banker = input("Give me everybody's name seperated by a comma. ")
# name = name_of_banker.split(", ")
# print(len(name))
# random_choice = random.randint(0,5)
# person_who_will_pay = name[random_choice]
# print(person_who_will_pay + " is going to buy the meal today. ")
'''if we write without split function it will take the whole person name as len '''
# name = input("Enter your name: ")
# print(len(name))
# random_choice = random.randint(0,5)
# who_will_pay_the_bill = name[random_choice]
# print(who_will_pay_the_bill + " is going to pay the bill ")
# name_of_friends = input("Enter all the name seperate by a comma: ")
# name = name_of_friends.split(", ")
# length = len(name)
# print(length)
# random_choice = random.randint(0,length)
# who_give_party = name[random_choice]
# print(who_give_party + " is going to give party. ")


# friends_name = input("Enter the name of your friends seperated by comma: ")
# name = friends_name.split(", ")
# length = len(name)
# select = random.randint(0,length)
# who_give_party = name[select]
# print(who_give_party + " is going to pay for treat. ")


friends_name = input("enter the name of friends seperated by comma: ").split(",")
length = len(friends_name)
select = random.randint(0,length)
who_give_party = friends_name[select]
print(f"{who_give_party} is going to give the paty ")
