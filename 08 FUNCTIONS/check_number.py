# Write a function check number even or odd
def check_number(number):
    if(number % 2 == 0):
        print(f"{number} is even number..")
    else:
        print(f"{number} is odd number..")

number = int(input("Enter A Number: "))
check_number(number)

