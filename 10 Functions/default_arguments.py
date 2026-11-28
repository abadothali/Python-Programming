# Q) Default Arguments -
# ->A default argument is a value assigned to a function parameter. If the user does not provide a value when calling the function, Python automatically uses the default value.

def greet(name = "Coder.."):
    print(name)

def message(msg = "Good Morning!"):
    print(msg)


message()
greet()
message("Good After Noon")
