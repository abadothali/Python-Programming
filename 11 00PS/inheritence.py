# Inheritance -

class Car:
    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stoped..")

class Bmw(Car):
    def __init__(self,name,color):
        self.name = name
        self.colr = color
        
        self.start()

    # We Can Access Also Using Parent Claas name -
    # Car.start()
    # Car.stop()

    def start(self):
        super().start()

bmw1 = Bmw("Royal","Red")
bmw1.start()



