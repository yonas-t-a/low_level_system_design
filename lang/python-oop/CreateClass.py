'''
Crate Class
'''

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, newName):
        self.name = newName

    def setAge(self, newAge):
        self.age = newAge




if __name__ == "__main__":
    person = Person("Tom", 40)
    print(person.name)
    print(person.age)