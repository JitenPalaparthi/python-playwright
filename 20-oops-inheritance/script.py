
class Animal:

    def __init__(self,name):
        self.name=name

class Dog(Animal):

    def __init__(self,name,breed):
        super().__init__(name)
        self.breed= breed

class Cat(Animal):

    def __init__(self,name,breed,colour):
        super().__init__(name)
        self.breed= breed
        self.colour=colour

d = Dog("Tommy","Labrador")

print("Dog Name:",d.name,"Dog Breed:",d.breed)
c = Cat("Phini","Some Cat","Black")

print("Cat Name:",c.name,"Cat Breed:",c.breed,"Colour:",c.colour)


