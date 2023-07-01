class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def make_sound(animal):
    print(animal.sound())

animal1 = Animal()
dog1 = Dog()
cat1 = Cat()

make_sound(animal1)  # No output (Animal class does not implement sound())
make_sound(dog1)    # Output: Woof!
make_sound(cat1)    # Output: Meow!
