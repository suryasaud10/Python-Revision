class Animal:
    def __init__(self, name):
        self.name = name

    # instance method
    def displayAnimalName(self):
        print(self.name)


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name) 

    # instance method
    def speaks(self):
        print(f"{self.name} barks")
    
dog_one = Dog("Tommy")
dog_one.speaks()
