class Account:
    def __init__(self,number,blance):
        self.number = number
        self.blance = blance

    # Debit -
    def debit(self,amount):
        self.blance -= amount
        print("Debit Money: ",amount)
        print("Availabel Blance:",self.blance)

    def credit(self,amount):
        self.blance += amount
        print("Credit Money: ",amount)
        print("Availabel Blance:",self.blance)

    def check_blance(self):
        print("Availabel Blance:",self.blance)



Sbi = Account(number="SBI1022700",blance=10000)
print("Account Number:",Sbi.number)
print("Total Blance:",Sbi.blance)

Sbi.debit(1000)
Sbi.credit(2000)
Sbi.check_blance()
Sbi.debit(1000)
Sbi.check_blance()




