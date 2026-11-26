# We can perfor operations in set such as add, remove etc
"""s = {1,2,3,4}
print(s)
s.add(5)
print(s)
s.remove(1)
print(s)"""

# frozen set: when we use frozen set we can't change anything..
s = frozenset({1,2,3})
print(s)
print(type(s))

for i in s:
    print(i)

