# enemies = "skeleton"
# def increase_enemies():
#     enemies = "zombie"
#     print(f"enemies inside function: {enemies} ")
# increase_enemies()
# print(f"enemies outside function: {enemies} ")

''' we have to never try to change the global scope because it can't work properly.'''
# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies} ")
# increase_enemies()
# print(f"enemies outside function: {enemies} ")


enemies = 1
def increase_enemies():
    global enemies
    enemies +=5
    print(f"enemies inside function: {enemies} ")
increase_enemies()
print(f"enemies outside function: {enemies} ")