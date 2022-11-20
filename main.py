class Dog:
    def woof(self):
        print("woof woof")


class Beagle(Dog):
    def woof(self):
        super().woof()
        print("super woof")


beagle = Beagle()
beagle.woof()
