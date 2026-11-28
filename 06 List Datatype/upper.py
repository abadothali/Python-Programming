# print names in upper case.
names = ["ram","shyam","mayan"]
names_upper = []

# Print name in upper case using loop -
"""for i in names:
    names_upper.append(i.upper())

print(names_upper)"""

# Using list Comprehension -
names_upper = [i.upper() for i in names]
print(names_upper)
