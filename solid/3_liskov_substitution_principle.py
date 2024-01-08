"""
The principle states that:
Subtypes must be substitutable for their base types.
Objects of a superclass should be able to be replaced with objects of a subclass without affecting the correctness of the program.
See this: https://medium.com/@m.nusret.ozates/solid-principles-with-python-245e45f9b1f8
See this: https://chat.openai.com/c/7f65bf38-27b0-4d1f-9d9e-6681ddffa0ae
"""


class Bird:
    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")


class Penguin(Bird):
    def swim(self):
        print("Penguin can swim")


# Function accepting objects of the Bird class
def make_bird_fly(bird):
    bird.fly()


# Using Liskov Substitution Principle
sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)  # Output: Sparrow can fly
make_bird_fly(penguin)  # No error, even though Penguin can't fly
