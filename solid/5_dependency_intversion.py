"""
1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.
"""


# Abstraction
class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


# Low-level module
class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: On")

    def turn_off(self):
        print("LightBulb: Off")


# High-level module
class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        if isinstance(self.device, Switchable):
            self.device.turn_on()
            self.device.turn_off()


# Usage
bulb = LightBulb()
switch = Switch(bulb)
switch.operate()
