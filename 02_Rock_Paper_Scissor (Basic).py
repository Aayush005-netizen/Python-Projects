import random

user_wins = 0
comp_wins = 0
options = ["rock", "paper","scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Invalid Choice")
        continue

    random_number = random.randint(0,2)
    comp_input = options[random_number]
    print(f"Computer picked {comp_input}.")

    if user_input == "rock" and comp_input == "scissors":
        print("You Won!")
        user_wins += 1
        continue
    elif user_input =="paper" and comp_input == "rock":
        print("You Won!")
        user_wins += 1
        continue
    elif user_input =="scissors" and comp_input == "paper":
        print("You Won!")
        user_wins += 1
        continue
    elif user_input == comp_input:
        print("Draw")
        continue
    else:
        print("You Lost!")
        comp_wins += 1
    
print(f"You won {user_wins} times.")
print(f"Computer won {comp_wins} times.")
print("Goodbye!")