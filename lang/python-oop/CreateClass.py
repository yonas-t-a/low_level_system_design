'''
Crate Class
'''

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age



if __name__ == "__main__":
    person = Person("Tom", 40)
    print(person.name)
    print(person.age)