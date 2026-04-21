"""
tuple is a immutable data types of python
support dublicate data
inclosed inside parenthesis()
Data cannot be changed here
can cointain mltiple types of data
"""


a = (1,2,3,4,5,6,"a")
print(type(a))

b = list(a)
b[0] = "Surya"

a = tuple(b)
print(a)

