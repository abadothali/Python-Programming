num1 = input("Enter A Number:")

try:
    int(num1)
    print(num1)
except:
    print("Some Error Ocured..")
finally:
    print("I am Always Execute..")

