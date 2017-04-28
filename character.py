# !/usr/bin/env python
# -- coding: UTF-8 --

class Character(object):
    def __init__(self, health, xp):
        self.name = name
        self.length = 0
        self.weight = 0
        self.nb_of_leg = nb_of_leg
        self.health = 100

    def feed(self):
        self.health += 1

    def move(self):
        self.health -= 1

    def sound(self):
        pass
