class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary= salary

    def print(self):
        return f"Name is {self.name}, salary is {self.salary}"


obj1= Employee("Siddhi", 5000000)
print(obj1.print())
