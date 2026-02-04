# string
# string is a sequence of characters enclosed within single or double quotes or triple quotes.
# Strings are used to represent text in Python.

a = "Hello, World!"
print(a)
print(type(a))

# Strings are Arrays

b = "Hello, Python!"
print(b[0])  # Accessing first character    
print(b[7])  # Accessing eighth character

# Looping Through a String

for x in "banana":
    print(x)

# String Length 
c = "Hello, World!"
print(len(c))


# Check String
txt = "The best things in life are free!"
print("Ram" in txt)


# Check if NOT
txt = "The best things in life are free!"   
print("Ram" not in txt)

# Slicing
b = "Hello, Python!"
print(b[2:5])  # characters from index 2 to 4


# Slice From the Start
b = "Hello, Python!"
print(b[:5])  # characters from the beginning to index 4

# Slice To the End
b = "Hello, Python!"        
print(b[2:])  # characters from index 2 to the end

# Negative Indexing
b = "Hello, Python!"    
print(b[-5:-2])  # characters from index -5 to -3


# Modify Strings

# upper case
a = "Hello, World!"
print(a.upper())

# lower case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
# white space is the space at the beginning or the end of a string.

a = " Hello, World! "
print(a.strip())  # returns "Hello, World!" without the leading and trailing whitespace

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))  # returns "Jello, World!"


# Split String
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # returns "Hello World"


# String Format
age = 36    
txt = "My name is John, and I am " + str(age)
print(txt)  # returns "My name is John, and I am 36"


#  f string
age = 36
txt = f"My name is John, and I am {age}"    
print(txt)  # returns "My name is John, and I am 36"