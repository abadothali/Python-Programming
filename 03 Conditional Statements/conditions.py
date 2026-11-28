# Conditions statement -
age = int(input("\nEnter Your Age:"))

if age >= 18 :
    print("You are Eligable For Vote..")
    if age >= 23 :
        print("You Can Drive Also..")
    else:
        print("You Can't Drive..")

elif age > 0 or age < 18 :
    print("You are not eligable for vote..")

elif age == 0:
    print("Please Input Your Actual Vote..")

else:
    print("Invalid Input..")


print("Code Execution Complete..")

