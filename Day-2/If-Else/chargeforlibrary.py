

nd = int(input("Enter number of days the book is kept: "))

if nd <= 5:
    amt = 2*nd

elif nd <= 6 and nd <= 10:
    amt = 3*nd

elif nd <= 11 and nd <= 15:
    amt = 4*nd
else:
    amt = 5*nd

print(f"The total charge for the library is: {amt} rupees")