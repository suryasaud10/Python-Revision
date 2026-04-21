import random
choices = ["p","s","r"]
while True:
    comp = random.choice(choices)
    print(comp)

    user = input("p/s/r:").lower()
    if user not in  choices:
        print("Invalid, Please enter valid data")
        break


    if user == comp:
        print("Game Draw")

    elif (user == "p" and comp == "r") or\
         (user == "r" and comp == "s") or\
         (user == "s" and comp == "p"):
        print("You WIn")
        break

    else:
        print("You Loose")