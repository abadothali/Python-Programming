"""
1) why we use set data type?
-> Unique data store
-> it's unorder data type

"""

"""x = {
"rahul",
"ram",
"ram",
"rahul",
"bhim",
"shyam",
"bhim",
"shyam"
}

print(x)
print(type(x))"""

# Right way to assign set -
"""x = [1,2,3,4]
print("Before set function use -")
print(x)
print(type(x))"""

"""print("After set function use -")
x = set(x)
print(x)
print(type(x))
"""
"""x = set((1,2,3,4))
print(x)
print(type(x))
"""

# Set Some Function -
"""x = {1,2,3}
y = {4,5,6}

print(x | y)
print(x & y)
"""

# we can't store list in set becuse list is changable.
x = {1,2,3,(1,2),"monirul",(1,2),[3,4]}
print(x)
