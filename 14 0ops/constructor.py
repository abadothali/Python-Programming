# Q) What is a Constructor?
# -> A constructor is a special method inside a class. It runs automatically. when we create a new object. It always takes a parameter called 'self'.


# Example:
class Student:

  # Constructor -
  def __init__(self):
    print("Constructor runs automatically...")


student1 = Student()
# Output: Constructor runs automatically...


# Q) Types of Constructors:
# -> There are two types of constructors:
#  1. Default Constructor (takes only 'self', no extra inputs)
#  2. Parameterized Constructor (takes 'self' plus extra inputs)


# 1) Example of Default Constructor:
class Student:

  def __init__(self):
    print("Default Constructor...")


s1 = Student()


# 2) Example of Parameterized Constructor:
class Student:

  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    print(f"Name of the student is: {self.name} and marks is: {self.marks}")


s1 = Student("Ram", 90)

