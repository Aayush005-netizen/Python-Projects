import random

user_wins = 0
comp_wins = 0
optionsDict = {"r":1, "p":2,"s":3}
options = {1:"rock", 2:"paper", 3:"scissors"}
while True:
    you = input("Enter Your Choice (r for stone, p for paper, s for scissors) or q to quit : ").lower()
    if you == "q":
        break
    comp_num = random.choice([1, 2, 3])
    you_num = optionsDict[you]
    print(f"You Chose {options[you_num]}")
    print(f"Computer Chose {options[comp_num]}")
    diff = comp_num - you_num
    if(diff == 1 or diff == -2):
        comp_wins += 1
        print("You Lost :(")
    elif diff ==0:
        print("It is a draw :|")
    else:
        print("You Won :)")
        user_wins += 1

print(f"You won {user_wins} times.")
print(f"Computer won {comp_wins} times.")
print("Goodbye!")