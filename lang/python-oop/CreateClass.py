'''
Goal:
    Creat a class called Person, 
'''

class Person:
    # class variable
    species = "human"

    def __init__(self, name: str, age: int):
        # Object instance, instance variable
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, newName):
        self.name = newName

    def set_age(self, newAge):
        self.age = newAge



if __name__ == "__main__":
    person = Person("Tom", 40)
    print(person.name)
    print(person.age)

    print(Person.species, "is the same us", person.species)
    # get the name and age via setter and getter

    def callGetters():
        name = person.getName()
        age = person.getAge()

        print(f'name = {name} \n Age = {age}')

    callGetters()

    person.setName("Alice")
    person.setAge(50)

    callGetters()