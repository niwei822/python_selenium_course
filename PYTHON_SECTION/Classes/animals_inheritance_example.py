

class Animal:

    def __init__(self, color, food_type):
        print("I am init.")
        self.color = color
        self.food_type = food_type

    def move(self):
        print("Animal moves")

    def eat(self):
        print("Animal eat")
        print("This animal eats {}".format(self.food_type))

    def breath(self):
        print("Animal breath")


class Dog(Animal):

    def __init__(self, color, food_type, breed, name):
        super().__init__(color, food_type)
        self.dog_breed = breed
        self.dog_name = name

    def bark(self):
        print("woofff")

    def as_security(self):
        print("My dog is my home security")

class Cat(Animal):

    def __init__(self, breed, name):
        self.cat_breed = breed
        self.cat_name = name

    def meaw(self):
        print("Meawwww")

mydog = Dog("Brown", "Meat", "Bulldog", "Max")
print(mydog.dog_breed)
print(mydog.dog_name)
mydog.eat()

# mycat = Cat("xyz", "yyy")
# mycat.eat()
# mycat.meaw()