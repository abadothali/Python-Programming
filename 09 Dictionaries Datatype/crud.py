# Create Operations-
"""student = {
"name":"Abadoth Ali Khan",
"age":25,
"height":5.8,
"isAdult":True
}"""

# Create Operations -
student = {}
student["id"] = 101
student["name"] = "Abadoth Ali Khan"
student["height"] = 5.8

# Read Operations -
print("Read Operations -")
print(student)
print(student["name"])
print(student.keys())
print(student.values())
print(student.items())

# Update Operations -
print("Update Operations -")
student.update({"isAdult":True, "city": "Kolkata"})
print(student)

# Delete Operations -
del student["id"]
print("Delete Operations -")
print(student)

