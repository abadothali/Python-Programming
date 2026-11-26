# 1) What is operators??
# -> Operatos basically used for some kind of operations in operands, like mathematic, logical, comparesions, bitwise and others.

# 2) Types of Operators??
# -> i) Assignment operator, ii) Arithmetic operator, iii) Comparison operators, iv) Logical operator, v) Identity operator, vi) Membership operators, vii) Bitwise operators

#) 1) Arithmetic operator - used for mathematics calculations.
a = 10
b = 20
print("Arithmetic Operations...")
print("Additions:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor Dividion:",a//b)
print("Modulus:",a%b)
print("Exponentiation:",a**b)


# 2) Assignment Operators - it's used for assign values or update values.
a = 10
b = a

print("Assignment Operations...")
print(a)
print(b)

# Remember this things - 
a += 2 # -> here add 2 number with previous value (10 + 2)
print(a)

a =+ 2 # -> here reset the value. 
print(a)

# we can perform also other operations like subtraction, multiplication etc..
x = 2
print(x)
x -= 2
print(x)

# 3) Comparision operator - it's used for compare one or more values.
x = 2
y = 4
print("Comparison operations...")
print("Equal: ", x == y)
print("Not Equal: ", x != y)
print("Geter Than: ", x > y)
print("Leser Than: ", x < y)
print("Greater than equal to: ", x >= y)
print("Less than equal to: ", x <= y)


# 4) Logical operator - it's used when we have multiple conditons.
x = 5
y = 10
print("Logical operator...")
print("AND opertions -> ", (x > y) and (x == y))
print("AND operations -> ", x < y and x != y)

print("OR operations -> ", x == y or x < y)
print("NOT operations -> ", not x == y)

# 6) Identity operator - compare the memory locations
print("Identity operations..")
x = [1,2,3,4]
y = [1,2,3,4]
z = x
print(x == y)
print(x is y)
print(x is z)
print(y is not z)

# 7) Membership Operations - it's chek whether value is exist or not
name = ("monirul", "ram")
print("Membership operations...")
print("monirul" in name)
print("rahul" not in name)
print("rahul" in name)

fact = 'i love python'
print("python" in fact)








