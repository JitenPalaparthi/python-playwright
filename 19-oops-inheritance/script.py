# parent - base
# child  - derived

# child class use them as is
# child class override them
# child class can extend them

class Animal:
    def speak(self):
        print("Animal makes some sound")

class Dog(Animal):
    pass

d = Dog()

d.speak()


## Method overriding

print("method overriding")

class Animal:

    def speak(self):
        print("Animal makes some sound")

class Dog(Animal):
     
     def speak(self):
        print("Dog barks")


d = Dog()

d.speak()

## call the parent method in the derided class 


print("call the parent method in the derided class ")

class Animal:

    def speak(self):
        print("Animal makes some sound")

class Dog(Animal):
     
     def speak(self):
        # call the base class method as well 

        super().speak()
        print("Dog barks")


d = Dog()

d.speak()



