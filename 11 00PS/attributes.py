# Q) What is attributes??
# -> Basically attributes are variables that belong to a class or an object. used to store data and characteristic. [char + act + teris + tic]

# Q) Types of attributes??
# -> Two types - class attributes and object (instance) attributes.

class student:

    # Class Attributes - it's shared by all -
    course = "Cyber Security"


    def __init__(self,name):
        # instance (object) attributes -
        self.name = name

# Object -
s1 = student("monirul")
print(s1.name)

