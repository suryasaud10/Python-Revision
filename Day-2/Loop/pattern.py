# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1

# Pattern using nested while loop in Python
for i in range(0, 5):
    for j in range(0, 6 - i):
        print(j , end=" ")
    print("")