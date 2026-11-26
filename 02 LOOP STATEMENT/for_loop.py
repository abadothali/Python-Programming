# Print Manualy repeted code, it's good to use loop

for step in range(1,6):
    print("Step",step)

for i in range(1,5):
    print("Hello!")
    if i >= 1:
        print(i)

# Print 1 to N Natural number and disply their sum:
number = int(input("Enter Your Number: "))
total = 0
for i in range(1,number+1):
    total += i

print(total)



