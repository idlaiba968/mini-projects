# import random

# emojis = {'r': '🧱', 'p': '📰', 's': '✂'}
# choices = ('r', 'p', 's')

# while True:
#     user_choice = input("Rock, Paper, or Scissor? (r/p/s): ").lower()
#     if user_choice not in choices:
#         print("Invalid Choice!")
#         continue

#     computer_choice = random.choice(choices)

#     print(f"User chose {emojis[user_choice]}")
#     print(f"Computer chose {emojis[computer_choice]}")

#     if user_choice == computer_choice:
#         print("Tie")
#     elif (
#         (user_choice == 'r' and computer_choice == 's') or 
#         (user_choice == 's' and computer_choice == 'p') or
#         (user_choice == 'p' and computer_choice == 'r')): 
#         print("You Loose!")
#     else:
#         print("You Won")

#     should_continue = input("continue? (y/n): ").lower()
#     if should_continue == 'n':
#         print("Thank You For Playing!")
#         break














# # breaking down program into smaller manageble functions

# import random

# emojis = {'r': '🧱', 'p': '📰', 's': '✂'}
# choices = ('r', 'p', 's')

# def get_user_choice():
#     while True:
#         user_choice = input("Rock, Paper, or Scissor? (r/p/s): ").lower()
#         if user_choice in choices:
#             return user_choice
#         else:
#             print("Invalid Choice!")

# def display_choices(user_choice, computer_choice):
#     print(f"User chose {emojis[user_choice]}")
#     print(f"Computer chose {emojis[computer_choice]}")
    

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         print("Tie")
#     elif (
#         (user_choice == 'r' and computer_choice == 's') or 
#         (user_choice == 's' and computer_choice == 'p') or
#         (user_choice == 'p' and computer_choice == 'r')): 
#         print("You Loose!")
#     else:
#         print("You Won")

# def play_game():
#     while True:
#         user_choice = get_user_choice()

#         computer_choice = random.choice(choices)

#         display_choices(user_choice, computer_choice)

#         determine_winner(user_choice, computer_choice)

#         should_continue = input("continue? (y/n): ").lower()
#         if should_continue == 'n':
#             print("Thank You For Playing!")
#             break

# play_game()










# using DRY principle:

import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {ROCK: '🧱', PAPER: '📰', SCISSORS: '✂'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, or Scissor? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choice!")

def display_choices(user_choice, computer_choice):
    print(f"User chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")
    

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)): 
        print("You Won!")
    else:
        print("You Loose!")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("continue? (y/n): ").lower()
        if should_continue == 'n':
            print("Thank You For Playing!")
            break

play_game()