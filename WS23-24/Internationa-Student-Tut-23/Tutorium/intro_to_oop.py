import doctest

class Animal:

    species = "None"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__nickname = None
        print("Animal Created")

    def make_sound(self):
        raise NotImplementedError("Subclass has not implemented this yet")


class Cat(Animal):

    species = "Feline"

    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food

    def make_sound(self):
        print("Meaw")

    def scratch(self):
        print("The cat scratched you")

class Dog(Animal):
    """
    
    >>> (x = cat("brandy", 2, "fish")) isinstance Dog # Doesnt work is just an idea of
    how it could be tested
    True
    """
    species = "Canine"

    def __init__(self, name, age, food):
        super().__init__(name, age)
        self.food = food

    def make_sound(self):
        print("wouf wouf")


cat = Cat("carl", 4, "fish")
dog = Dog("t",1,"dry")

cat.make_sound()
cat.scratch()

dog.make_sound()

# Doesnt exist because was defiend only for the CAT
# dog.scratch()

if __name__ == "__main__":
    doctest.testmod()