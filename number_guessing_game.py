import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        user = int(input("Guess the number between 1 and 100: "))
        if user < 100 and user > 0:
            if user < number_to_guess:
                print("Too Low!")
            elif user > number_to_guess:
                print("Too High!")
            else:
                print(user, "is correct", "You Won!")
                break
        else:
            raise ValueError
    except ValueError:
        print("Please enter a valid number.")