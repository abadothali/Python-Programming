# Q) What is static method??
# -> it's basically a method that don't use self parameter. it's also caled decorator

class info:

    @staticmethod
    def msg():
        print("this is a important informations..")

info1 = info()
info1.msg()




