# Q) What is method??
# -> Basically Method is a function inside a class.

# Class -
class student:

    # Constructor -
    def __init__(self,name,school):
        self.name = name
        self.school = school

    # Method -
    def wellcome(self):
        print("Welcome:",self.name)
        print("Graduate from:",self.school)

# Object -
s1 = student("Developer","Herber Univercity")
s1.wellcome()
