class Employee:
    def __init__(self, name, roll):
        self.name= name
        self.roll = roll

    def print1(self):
        return f"Name is {self.name}, Roll is {self.roll}"


class Company(Employee):

    def print_com(self):
        return  f" Name is {self.name}"


object1= Company("Siddhi", 31)

print(object1.print_com())

