# def add():
#     print("This is add function")

# # call the function
# add()

# def greet(name):
#     print(f"Hello, {name}!!")

# greet("Surya")


# # default arguments

# def sum(a, b = 5):
#     print(f"The sum of {a} and {b} is {a + b}")

# sum(10)
# sum(10, 20) 

# # return statement
# def sum(a, b):
#     return a + b
# c = sum(10, 20)
# print(f"The sum of 10 and 20 is {c}")


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

def calculate(a, b):
    sum = a + b
    diff = a - b
    mul = a * b
    div = a / b
    return sum, diff, mul, div

s, d, m, di = calculate(a, b)

print("sum:", s)
print("diff:", d)
print("mul:", m)
print("div:", di)