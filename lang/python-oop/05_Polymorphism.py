class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"
    
if __name__ == "__main__":
    dog = Dog("Terry")
    cat = Cat("wor")
    print(dog.speak())
    print(cat.speak())
    
    animals = [Dog("Rex"), Cat("Mittens"), Dog("Max")]
    for animal in animals:
        print(animal.speak())