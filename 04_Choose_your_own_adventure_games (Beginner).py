name = input("Type your name: ")
print(f"Welcome {name}, to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, You can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked endlessly and died!")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, It look wobbly, do you want to cross it or head back (cross/back)? ").lower()
    if answer == "cross":
        answer = input("You crossed the bridge and met a stranger. Will you talk to them (yes/no)?").lower()
        if answer == "yes":
            print("You won!")
        elif answer == "no":
            print("You got lost and died!")
        else:
            print("Not a valid option. You lose!")
    elif answer == "back":
        print("You go back to main road and died beacuse bandits raided you!")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank You!!!")