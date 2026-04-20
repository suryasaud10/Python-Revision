import random
num = random.randint(1,20)
print(f"New random number is {num}")


comp = 0
person = 0

while True:
    computer = int(input("Enter the random number guessed by computer : "))



    if(computer == num):
        comp +=5
        print(f"point of computer is: {comp}")
        print("="*50)            

        num = random.randint(1,20)
        print(f"New random number is {num}")
        print("."*50)            

        if (comp == 15):
            print("Game over!! Computer win the game.")
            break

    user = int(input("Enter the random number guessed by user : "))

    if(user == num):
        person +=5
        print(f"point of User is: {person}")
        print("="*50)            

        num = random.randint(1,20)
        print(f"New random number is {num}")
        print("."*50)            


        if (person == 15):
            print("Game over!! User win the game.")

            break
    


