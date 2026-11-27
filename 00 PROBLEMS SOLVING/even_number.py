# Take a number n from the user, and print all even numbers.
def print_even(n):
    for i in range(1,n + 1):
        if i % 2 == 0:
            print(i,end=" ")

n = int(input("Enter A Number: "))
print_even(n)

