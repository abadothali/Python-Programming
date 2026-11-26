numbers = [1,2,3,4]
evens = []

"""
# Using loop -
for i in numbers:
    if i % 2 == 0:
        evens.append(i)
"""

# Using list comprehension -
"""evens = [i for i in numbers if i % 2 == 0]
print(evens)"""


# Check even or odd -
evens = ["Even Number!" if i % 2 == 0 else "Odd Number!" for i in numbers]
print(evens)
