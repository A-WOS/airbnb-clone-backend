class Player:

    def __init__(self, name, exp):
        self.name = name
        self.exp = exp

    def say_hello(self):
        print(f'hello my name is {self.name}')


awos = Player("awos", 1000)
print(awos.name, awos.exp)

awos.say_hello()
