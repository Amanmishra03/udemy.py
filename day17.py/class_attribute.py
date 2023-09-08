# class User:
#     pass

# user_1 = User()
# user_1.id = "001"
# user_1.username = "angela"
# print(user_1.username)
# print(user_1.id)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"
# print(user_2.id)

# constructer

class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
''' here in the above code in def line self is object. And user_id and username is parameter. 
    And self.id in below line of def is attribute. '''

user_1 = User("001", "angela")
user_2 = User("002", "jack")
user_4 = User("003" , "adarsh")
user_3 = User("004", "amjad")
print(user_1.id, user_1.username)

