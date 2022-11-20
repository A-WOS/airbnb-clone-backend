class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"hello my name is {self.name}")


class Player(Human):

    def __init__(self, name, exp):
        super().__init__(name)
        self.exp = exp


class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team


awos_player = Player("awos", 10)
awos_player.say_hello()
awos_fan = Fan("awos_fan", "dontknow")
awos_fan.say_hello()