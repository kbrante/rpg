#!/usr/bin/env python
# -- coding: UTF-8 --

from .item import Inventory

class Character(object):

   def __init__(self, health, xp):
       self.health = health
       self.xp = xp

   def eat(self, food):
       self.health += food.use()

   def move(self):
       pass

   def die(self):
       pass

   def receive_attack(self, damage):
       self.health -= damage


class Player(Character):

   def __init__(self,health,xp):
       Character.__init__(self, health, xp)
       self.inventory = Inventory(20)

   def pick(self, item):
       self.inventory.set_item(item)

   def drop(self, item):
       self.inventory.del_item(item)

   def fight(self, enemy):
       damage = 10
       enemy.receive_attack(damage)



class Chicken(Character):

   def __init__(self):
       Character.__init__(30, 1)
