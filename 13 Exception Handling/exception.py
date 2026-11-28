number = input("Enter A Number: ")

# Now Try To Print Table: it's nicely run when we input a integer number. it's give error when we inputs characters.
"""
print(f"Table Of {number}")
for i in range(1,11):
    print(f"{number} X {i} = {int(number) * (i)}")

"""

# Exception Handling -
print("\nException Handling..")
try:
    print(f"Table Of {number}")
    for i in range(1,11):
        print(f"{number} X {i} = {int(number) * (i)}")

except Exception as e:
    print(e)

print("Code Execution Complete..") 

