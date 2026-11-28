# Take input 10 items from the user in a list, and target an element. Search target elemet one by one in a list, if found target element print found and print index number. if not found print items not not found.

# Take input items from the user:
items = []
for i in range(10):
    items.append(int(input("Enter Items: ")))

# Print All Items: 
print(items)

# Take input target elment from the user:
target = int(input("Enter Your Target Element: "))

# Search target elemets:
f = 0
found = False
while f < len(items):
    if target == items[f]:
        print(target,"Found At Index Number:",f)
        found = True
        break
    f += 1

if not found:
    print(target,"Item not exist in a list..")

