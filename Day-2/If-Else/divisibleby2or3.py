# A program to check if a number is divisible by 2 or 3

a = int(input("Enter a number: "))
if a % 2 == 0 or a % 3 == 0:
    print(f"{a} is divisible by 2 or 3")
else:
    print(f"{a} is not divisible by 2 or 3")