class Animal:
    def __init__(self, name, birth_date, commands=[]):
        self.name = name
        self.birth_date = birth_date
        self.commands = commands

    def train(self, new_command):
        self.commands.append(new_command)

class HomeAnimal(Animal):
    pass

class PackAnimal(Animal):
    pass
