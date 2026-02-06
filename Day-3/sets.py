
sample_set = {1,"A",3.14,True}
print(sample_set)
print(type(sample_set))


num_list = [1,2,3,4,5,1,2,3,4,5]
num_set = set(num_list)
print(num_set)
print(type(num_set))

# empty set
empty_set = set()
print(empty_set)


bk_list = ["Python", "Java", "C++", "Python", "Java"]
book_list = set(bk_list)
for i in book_list:
    print(i)

book_list.update("JavaScript")
book_list.add('C#')
print(book_list)

# remove elements  
book_list.remove("Java")
book_list.pop()
print(book_list)


# set operations

A = {1,2,3,4,5}
B = {4,5,6,7,8}

# union
print(A | B)
print(A.union(B))

# intersection
print(A & B)
print(A.intersection(B))

# difference
print(A - B)    
print(A.difference(B))

# symmetric difference
print(A ^ B)    
print(A.symmetric_difference(B))

