
list = ['apple', 'banana', 'cherry', 'mango', 'orange', '12', '34', '56','1.1', '2.2']
print(list[1:5]) 




for i in list:
    print(i)


for i in range(len(list)):
    print(list[i])

list.append('grape')
print(list)

list.insert(2, 'kiwi')
print(list)

list.remove('12')
print(list)

list.pop()
print(list)