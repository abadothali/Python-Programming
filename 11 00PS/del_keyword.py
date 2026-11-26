# Del Keywords: Used For Delete For Objects And It's Poperty.

# Class -
class Student:
    def __init__(self,name):
        self.name = name

# Object -
s1 = Student("monirul")
print("Before Del Keyword Used -")
print(s1.name)

del s1.name
"""
print("After Del Keyword Used -")
print(s1.name)
"""

# We can Delete S1 Object itself.
print("Before S1 Object Delete -")
print(s1)

del s1
print("Afte Del Keyword Used -")
print(s1)


