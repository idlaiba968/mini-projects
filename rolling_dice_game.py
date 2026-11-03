# import random 
# ok = True
# while ok:
#     user = input("Roll the dice? (y/n): ").lower()
#     if user in ['yes', 'y']:
#         print(f"({random.randint(1, 6)}, {random.randint(1, 6)})")
        
#     elif user in ['n', 'no']:
#         print("Thanks for playing!")
#         break
#     else:
#         print("Invalid Input!")






import random

# loop
while True:
    #     ask: roll the dice
    choice = input("Roll the dice?").lower()
    #     if user enters y
    if choice == 'y' or choice == 'yes':
    #         generate two random numbers
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
    #         print them
        print(f"({num1}, {num2})")
    #     if user enters n
    elif choice == 'n' or choice == 'no':
    #         print thank you message
        print("Thank you for playing!")
    #         terminate
        break
    #     else
    else:
    #         print invalid choice
        print("Invalid Choice!")