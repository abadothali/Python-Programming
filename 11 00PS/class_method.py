# 3) Class Method (@classmethod - takes 'cls' parameter)
# -> Used to access or modify Class Attributes (shared by all objects).

class Student:
  # Class Attribute
  college = "Narula Institute Of Technology"

  def __init__(self, name):
    self.name = name

  # Class Method
  @classmethod
  def change_college(cls, new_college):
    cls.college = new_college


# Creating objects
s1 = Student("Abadoth")
s2 = Student("Ram")

print("Before:", s1.college)  # Output: Narula Institute Of Technology
print("Before:", s2.college)  # Output: Narula Institute Of Technology

# Calling Class Method using the Class name
Student.change_college("NIT Kolkata")

# Both objects get updated automatically!
print("After:", s1.college)  # Output: NIT Kolkata
print("After:", s2.college)  # Output: NIT Kolkata
