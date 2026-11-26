# Calculate simple intrest...
principal = float(input("Enter Actual money: "))
rate_of_intrest = int(input("Enter Rate Of Intrest: "))
time = int(input("Enter Time(in a year): "))

actual_interst = (principal * rate_of_intrest * time) / 100
total_money = principal + actual_interst

print("Money which you borrow:",principal)
print("Intrest rate per year:",rate_of_intrest,"%")
print("Borror for:",time,"year")
print("Actual interest:",actual_interst)
print("Totail money:",total_money)

