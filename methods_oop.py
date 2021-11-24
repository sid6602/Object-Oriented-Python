class Employee:

    def print(self):
        return f"Name is {self.name}, salary is {self.salary}"


obj1= Employee()

obj1.name = "Siddhi"
obj1.salary = 5000000

print(obj1.print())
