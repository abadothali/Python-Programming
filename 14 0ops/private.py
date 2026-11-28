# Private Attributes | Private Method 
class Student:
    # Private (double underscore)
    __name = "Abadoth Ali Khan"

    """
    def __init__(self,name):
        self.name = name

        """
    
    def name_print(self):
        print(f"wellcome:{self.__name}")
    

s1  = Student()
s1.name_print()
