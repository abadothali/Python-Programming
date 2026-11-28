class student:
    def greating(self):
        print("Hey:",self.name)

    def __init__(self,name):
        self.name = name


s1 = student("Developer")
print("Before update...")
s1.greating()

# Operations - We can update value.
s1.name = "Software Developer"
print("After update...")
s1.greating()


