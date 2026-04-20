import random

step = 0
num = random.randint(10,15)
print(num)
gussed_attempt = 5

while(True):
    step += 1

    user = int(input("Enter the random number:"))
    if(user == num):
        print("You have complated the game in", step)
        string = input("Do You want to play again? y/n")
        if (string  == 'y'):
            num = random.randint(10,15)
            print(num)
            step = 0
        else:
            print("thank you")
            break

    else:

        gussed_attempt = gussed_attempt - 1
        print(f"remmaing attempts is {gussed_attempt}") 
         
        if(gussed_attempt == 0):
            play = input("Do you want to play again y/n? ")
            if(play == "y"):
                num = random.randint(10,15)
                print(num)
                gussed_attempt = 5
            else:
                print("Thank You for Playing game")
                break
        





