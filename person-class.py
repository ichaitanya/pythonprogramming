class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


john = Person("Johnny")
john.talk()

bob = Person('BobbOWE')
bob.talk()