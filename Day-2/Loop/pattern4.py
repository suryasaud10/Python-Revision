# 5 5 5 5 5
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5

# Pattern using nested while loop in Python
for i in range(1, 6):
    for j in range(6, i, -1):
        print(5, end=" ")
    print("")