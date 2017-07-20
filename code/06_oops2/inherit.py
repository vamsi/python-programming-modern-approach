class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Pet):
    def sound(self):
        print("Bow Bow..")


class Cat(Pet):
    def sound(self):
        print("Meow Meow..")


class Parrot(Pet):
    def sound(self):
        print("Hello I am {}".format(self.name))


# pet 1
p1 = Dog("Dozer", 4)

# pet 2
p2 = Parrot("Django", 6)

# pet 3
p3 = Cat('Edward', 3)
print(p1.name, p1.age)

p1.sound()
print(p2.name, p2.age)
p2.sound()
print(p3.name, p3.age)
p3.sound()
