# create a list and print their squar.
"""
1) Manualy -

list = [1,2,3,4,5]
squars = []

for i in list:
    print(i)
    squar = i * i
    squars.append(squar)

print(squars)


"""

list = [1,2,3,4,5]
squar = [i * i for i in list]
print(list)
print(squar)


