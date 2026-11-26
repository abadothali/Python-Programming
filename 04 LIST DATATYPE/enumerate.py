# create a list and print all elements with indexing.
names = ["Monirul","Nikita","Rupsha","Gautam","Ravi"]

# Using loop -
"""for i in range(len(names)):
    print(i,names[i])
"""
# OR
"""for i in range(len(names)):
    print([i,names[i]])"""

# Using Enumeret function -
for i,name in enumerate(names):
    print(i,name)

# Using list comprehension -
"""name = [[i,names[i]] for i in range(len(names))]
print(name)
print(type(name))
"""

