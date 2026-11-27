# Print the factorial of N
# Function definitions -
def fact(n):
    calculate_factorial = 1
    for i in range(1,n+1):
        calculate_factorial *= i
    print(f"Claculate Factorial Of {n} is: {calculate_factorial}")


number = int(input("Enter A Number: "))
fact(number)