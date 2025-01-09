print("Welcome to my Computer Quiz!!!")
playing = input("Do you want to play?(Yes/No) ")
a=0
q=0
if playing.lower() != "yes":
    quit()

print("\tOkay! Let's Play:)")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("\tCorrect!")
    a+=4
    q+=1
else :
    print("\tIncorrect!")
    a-=1


answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("\tCorrect!")
    a+=4
    q+=1
else :
    print("\tIncorrect!")
    a-=1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("\tCorrect!")
    a+=4
    q+=1
else :
    print("\tIncorrect!")
    a-=1

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("\tCorrect!")
    a+=4
    q+=1
else :
    print("\tIncorrect!")
    a-=1

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("\tCorrect!")
    a+=4
    q+=1
else :
    print("\tIncorrect!")
    a-=1

print(f"You got {q} questions correct")
print(f"You got {a} points and your percentage is {(a/20) * 100}% ")

