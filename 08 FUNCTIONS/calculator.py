# Additions -
def additions(number1,number2):
    print(number1 + number2)

# Substraction -
def substractions(number1,number2):
    print(number1 - number2)

# Multiplecations -
def multiplecations(number1,number2):
    print(number1 * number2)

# Divisions -
def division(number1,number2):
    print("1) Choose 1 For Division:")
    print("2) Choose 2 For Floor Division:")
    choose = int(input("Choose A Number: "))

    if choose == 1:
        print(number1 / number2)
    elif choose == 2:
        print(number1 // number2)
    else:
        print("Invalid Input..")



while True:
    print("-----------------CALCULATOR APPLICATIONS-----------------")

    number1 = int(input("Enter First Number: "))
    number2 = int(input("Enter Second Number: "))

    print("Type 1 For Additions -")
    print("Type 2 For Substraction -")
    print("Type 3 For Multiplecations -")
    print("Type 4 For Divisions -")
    print("Type Exit for Stop This Appications -")
    choose = input("Enter Your Operations: ")


    match choose:
        case "1": additions(number1,number2)
        case "2": substractions(number1,number2)
        case "3": multiplecations(number1,number2)
        case "4": division(number1,number2)
        case "Exit" : break
        case _: print("invalid operations Choose")





