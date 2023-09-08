enemies = 1

def increase_enemies ():
    enemies = 2
    print(f"enemies inside function: {enemies} ")

increase_enemies ()
print(f"enemies outside function: {enemies} ")

# local scope exist within function

def drink_portion ():
    portion_strength = 2
    print(portion_strength)

drink_portion()
# print(portion_strength)

'''print(portion_strength) this cannot be printed because it is local scope
 and we try to print it in global scope
 we can print a global scope in local scope but vice versa is not possible''' 

# global scope
player_health = 10
def drink_portion ():
    portion_strength = 2
    print(player_health)

drink_portion()

'''if we create a variable within a function then it is only within a function
 and if we create a variable within in if block or while loop or for loop then 
 it is not count in local scope. '''

game_level = 3
def create_enemy():
    enemies = ["skeleton", "zombie", "Alien"]
    if game_level <5:
        new_enemy = enemies[0]
        print(new_enemy)

create_enemy()

game_level = 3
enemies = ["skeleton", "zombie", "Alien"]
if game_level <5:
    new_enemy = enemies[0]
print(new_enemy)