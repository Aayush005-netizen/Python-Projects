import random

def roll():
    roll = random.randint(1,6)
    return roll

while True:
    players = int(input("Enter the numbers of players playing (2 - 4): "))
    if 2 <= players <= 4:
        break
    else:
        print("There should be 2 to 4 players")

max_score = int(input("Enter the Upper Limit of the Game: "))
player_scores = [0 for _ in range(players)]   #[0,0,0,0] for players = 4

while max(player_scores) < max_score:

    for players_index in range(players):
        print("\nPlayer", players_index + 1, "turn has just started!\n")
        print("Your total Score is:", player_scores[players_index], "\n")
        current_score =0

        while True:
            should_roll = input("Whould you like to roll (y)? ")
            if(should_roll.lower() != "y"):
                break
            
            value = roll()
            if value == 1:
                current_score =0
                print("You rolled a 1! Turn done!")
                break
            else:
                current_score += value
                print("You rolled a:",value)
            
            print("Your score is:",current_score)

        player_scores[players_index] += current_score
        print("Your total Score is:", player_scores[players_index])

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player number", winning_index + 1, "is the winner!!!")