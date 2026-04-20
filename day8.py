"""
for loop

"""
# for loop in touple
# for i in [1,2,3,4,5,1]:
#     if (i%2 == 0):
#         print(f"{i} even")
#     else:
#         print(f"{i} odd")


# #  dor loop in dictionary
# a = {
#     "name": "Hari",
#     "collage": "NAST"
# }

# for i in a:
#     print(f'{i}= {a[i]}')

# for i in a.values():
#     print(i)


# for i in range(1,10,1):
#     print(i)

# # convert loops into list
# even= []
# odd = []
# for i in range(1,20):
#     if (i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"{even} are even number")
# print(f"{odd} are odd number")

# continue and break 
a = [1,2,3,4, "hello", "test", 1,2,3,7.3, True]
# for i in a:
#     if type(i) != int :
#         continue
#     else:
#         print(i)

# use this rather above bcz during object id comparing it does not couse error
for i in a:
    if not isinstance(i, str):
        print(i)

# b = [10,20,30,40]
# sum =0
# for i in b:
#     sum += i
# print(sum)


# for i in [1,2,3]:
#     for j in [4,5,6]:
#         print(i,j)
