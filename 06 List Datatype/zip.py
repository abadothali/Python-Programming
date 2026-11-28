name = ["monirul","Abul","Parmina"]
age = [25,23,20]

# Using Loop -
"""for i in range(len(name)):
    print(name[i],age[i])"""


# Using zip function -
"""for name,age in zip(name,age):
    print(name,age)"""

# Using List Comprehension -
details = [[name[i],age[i]] for i in range(len(name))]
print(details)

