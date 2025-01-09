import random

top_of_range = input("Type a number: ")
if(top_of_range.isdigit()):
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("\tPlease type Natural Numbers!")
        quit()
else:
    print("Please type a digit")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True:

    user_input = input("Enter your Guess: ")
    guesses += 1
    
    if(user_input.isdigit()):
        user_input = int(user_input)
    else:
        print("Please type a digit")
        continue

    if user_input == random_number:
        print("You Got it Correct!")
        break
    elif user_input > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print(f"You took {guesses} guesses!")
