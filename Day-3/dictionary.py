

# empty dictionary
empty_dict = {}
print(empty_dict)


# dictionary with key-value pairs
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person["name"])
print(person.keys())

print(person.values())
print(person.items())


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
# update dict1 with dict2
dict1.update(dict2)
print(dict1)


dict1.update({"a": 10})
print(dict1)