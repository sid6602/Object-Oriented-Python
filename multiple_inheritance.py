class Employee:
    def __init__(self, name):
        self.name= name

    def namee(self):
        return f"Name is: {self.name}"


class Player:
    def __init__(self, game):
        self.game = game

    def gamee(self):
        return f"Name is: {self.game}"

class Emp_player(Employee, Player):


    language= "python"
    def lang(self):
        print(self.language)

object1= Employee("Siddhi")
object2= Player("Cricket")
object3= Emp_player("Sid")

print(object3.namee())
print(object3.lang())
