from time import sleep
from threading import *

class People(Thread):
    # run is a built in method of Thread class, which we are overriding here
    def run(self):
        for i in range(5):
            print("People are walking")
            sleep(1)

class Car(Thread):
    # run is a built in method of Thread class, which we are overriding here
    def run(self):
        for i in range(5):
            print("Cars are moving")
            sleep(1)

    
people = People()
car = Car()

""" 
start is a built-in method of thread, It arranges for the 
object's run() method to be invoked in a separate thread of control.
"""
people.start()
car.start()

# Output will be look like this
    # People are walking
    # Cars are moving
    # Cars are moving
    # People are walking
    # People are walking
    # Cars are moving
    # People are walking
    # Cars are moving
    # People are walking
    # Cars are moving