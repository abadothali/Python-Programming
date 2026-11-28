# We can create custom error -

"""
number = int(input("Enter A Number Between Five To Nine: "))

if number < 5 or number > 9 :
    raise ValueError("number Should be Gater Than Five And less Than Nine..")

"""

class InvalidAgeError(Exception):
    pass

def checkAge(age):
    if age < 18:
        raise InvalidAgeError("Age Should be gater than 18")
    print("Access Gurented..")

checkAge(10)

