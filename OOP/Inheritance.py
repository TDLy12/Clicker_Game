class Animal():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print("I am an animal")

    def describe(self):
        print(self.name + (" ") + str(self.age) + (" ") + self.color)

    def tricks(self):
        print("I can do a trick")

class Bird(Animal):
    def speak(self):
        super().describe()
        print("I am a bird")

    def tricks(self):
        print("I can do a trick")

    def fly(self):
        print("I am flying!")


class Cat(Animal):
    def speak(self):
        super().describe()
        print("I am a cat")

    def tricks(self):
        print("I can do a trick")

    def  scratch(self):
        print("I am scratching the sofa!")


class Dog(Animal):
    def __init__(self, name, age, color, legs):
        super().__init__(name, age, color)
        self.legs = legs

    def speak(self):
        super().describe()
        print("I am a dog")

    def tricks(self):
        print("I can do a trick")

    def guard(self):
        print("I am guarding the house!")

    def introduce(self, friend):
        self.speak()
        print("here is my friend,")
        friend.speak()

dog1 = Dog("Dog", 4, "grey", 4)
cat1 = Cat("Cat", 5, "black")
bird1 = Bird("Bird", 2, "white")

dog1.introduce(bird1)
