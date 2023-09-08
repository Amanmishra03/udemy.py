from random import randint
# welcome to the number guessing game 
# i am thinking of a number between 1 to 100
# choose a difficulty . Type 'easy' or 'hard'

def check_answer(guess,answer):
    if guess>answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print("you got it! The answer was {answer}. ")
# make function to set difficulty
# def set_difficulty():
#     level = input("choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS0


print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 to 100")
answer = randint(1,100)
guess = int(input("Make a guess: "))
