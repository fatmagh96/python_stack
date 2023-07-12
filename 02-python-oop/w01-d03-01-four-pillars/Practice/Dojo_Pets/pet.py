class Pet:
    def __init__(self,type,tricks,health,energy):
        self.type = type 
        self.tricks = tricks 
        self.health = health 
        self.energy = energy 
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print("Meow")
        return None
    
class Cat(Pet):
    def __init__(self, type, tricks, health, energy):
        super().__init__(type, tricks, health, energy)


class Dog(Pet):
    def __init__(self, type, tricks, health, energy):
        super().__init__(type, tricks, health, energy)

class Snake(Pet):
    def __init__(self, type, tricks, health, energy):
        super().__init__(type, tricks, health, energy)

class Hamster(Pet):
    def __init__(self, type, tricks, health, energy):
        super().__init__(type, tricks, health, energy)