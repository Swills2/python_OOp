class Animal:
    def __init__(self):
        self.name = name
        self.health = health

    def walk(self):
        health -= 1
        return self

    def run(self):
        health -= 5
        return self

    def displayHealth(self):
        print(health)
        
        return self

class Dog(Animal):
    def __init__(self):
        health = 150

        return self

    def pet(self):
        health += 5

        return self

class Dragon(Animal):
    def __init__(self):
        health = 170

        return self

    def fly(self):
        health -= 10

        return self

    def displayHealth(self):
        print(health)
        print("I am a dragon")

        return self




        