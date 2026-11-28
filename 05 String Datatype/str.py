"""name = input("Enter Your Name:")
print(name)
print(type(name))
print(len(name))"""

# String Conversions -
"""if name.title() == "Abadoth Ali Khan":
    print("Found!")
else:
    print("Not Found!")"""

# String Normalizations -
"""name = "monirul khan"
print(name.upper())
print(name.lower())
print(name.title())"""

# String indexing -
"""name = "Abadoth Ali Khan"
print(len(name))
print(name[0])
print(name[1])
print(name[5])
print(name[len(name)-1])"""

# Slicing -
"""name = "monirul khan"
print(type(name)) # -> <class - str>
print(len(name)) # -> 12
print(name[0:]) # monirul khan
print(name[:]) # monirul khan
print(name[2:]) # nirul khan
print(name[:len(name)]) # -> monirul khan
print(name[2:12]) # -> nirul khan
print(name[0::3]) # -> milh"""

# Method -
name = "monirul"
print(name.count("o"))
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
print(name.find("i"))