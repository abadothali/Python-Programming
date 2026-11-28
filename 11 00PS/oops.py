# OBJECT ORIENTED PROGRAMMING -

# Q) What Is Class??
# -> Class is a collection of property and methods of an object. or we can say it's blueprint of an object.


# Q) What IS Object??
# -> Object is a instance of a class. it's a real world entity. physically exist.


# Class - 
"""
class student:
    college = "Narula Institute Of Technology"

# Object -
Abadoth = student()
print(Abadoth.college)
print(student.college)
print(Abadoth)
print(type(Abadoth))

"""

# Q) Create a class of a student and store their college name, student name and marks and print output.

# Class -
"""
class student:
    # Class Attribute -
    college = "Narula Institute Of Technology"

    # Constructor -
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

# Object -
name = input("Enter Your Name: ")
marks = int(input("Enter Your Marks: "))
s1 = student(name,marks)
print(s1.college)
print(s1.name)
print(s1.marks)

"""



# Q) What Is Constructor??
# -> Constructor is a special type of function inside a clas. It's run autometically that time we create a new object. it's take a parameter it's called self.

# Example -
"""
class Student:

    # Constructor -
    def __init__(self):
        print("Constructor Run Autometically..")

student1 = Student()
# Output: Constructor Run Autometically..

"""


# Q) Types Of Constructor -
# -> Constructor Is Two Types First Is Default Constructor And Second is Parameterized Constructor.

# 1) What Is Default Constructor??
# -> Not Take Extra Inputs.


# Example Of Default Constructor -
"""
class student:

    # Default Constructor -
    def __init__(self):
        print("Default Constructor...")

s1 = student()

"""

# 2) What Is Parameterized Constructor??
# -> Takes Extra Inputs.


# Example Of Parameterized Constructor -
"""
class student:

    # Parameterized Constructor -
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(f"name of the student is:{self.name} and marks is:{self.marks}")

s1 = student("Ram",90)

"""



# Q) What Is Attributes??
# -> Basically Attributes are variables that belong to a class or an object. used for store data.

# Q) Types Of Attributes??
# -> Attributes are two types, First is Class Attributes and Second is Instance(object) Attributes.

# Example Of Attributes -

"""
class Student:
    # Class Attributes -
    college_name = "XYZ College"

    def __init__(self,name):
        # Instance (Object) attributes - 
        self.name = name

s1 = Student("Abadoth Ali Khan")
print(s1.college_name)
print(s1.name)

"""

# NOTES - We can also access class attributes directly using the class name itself, like print(Student.college_name), even without creating an object!

"""
class Car:
    model = "bmw"

print(Car.model)

"""




# Q) What is method??
# -> Basically method is a function inside of a class.

# Example Of Method - 
"""
class Student:
    # Constructor -
    def __init__(self,name):
        self.name = name

    # Method -
    def wellcome(self):
        print("Wellcome:",self.name)

# Object -
s1 = Student("Abadoth")
s1.wellcome()

"""

# Q) Types Of Methods??
# -> Static Method (Does not take self or cls parameter)
# -> Non Static Method (Take Self Parameter)
# -> Class Method (Take cls Parameter)

# Example Of Static And Non Static Method.

"""
class Student:
    # Constructor -
    def __init__(self,name):
        self.name = name

    # Static Method -
    @staticmethod
    def wellcome():
        print("Wellcome..")

    # Non Static Method -
    def user(self):
        print("Student Name:",self.name)

# Object -
s1 = Student("Abadoth")
s1.wellcome()
s1.user()

"""

# Example Of Class Method -

"""

# Class -
class Student:
    # Class Attributes -
    college_name = "XYZ College"

    # Constructor -
    def __init__(self,name):
        self.name = name

    # Class Method -
    def new_college(cls,newCollege):
        cls.college_name = newCollege

    # Non Static Method -
    def wellcome(self):
        print("Wellcome:",self.name)
        print("Graduate From:",self.college_name)


# Object -
s1 = Student("Ram")
print("Before Update College Name -")
print(s1.college_name)

s1.new_college("NIT KOLKATA")
print("After Update College Name -")
print(s1.college_name)

s1.wellcome()

"""

