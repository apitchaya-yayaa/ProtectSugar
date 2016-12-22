from arcade import key
import arcade
from random import randint
from random import random
from time import time
import math

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = angle

class Ant(Model):
    def __init__(self,world,x,y):
        self.velocity = 1
        diff_x = world.sugar.x - x
        diff_y = world.sugar.y - y
        rad = None
        if diff_x != 0 :
            rad = math.atan(float(diff_y) / diff_x)
        else :
            rad = math.pi / 2
        angle = math.degrees(rad)
        if(x > world.sugar.x) :
            angle += 180
        super().__init__(world, x, y, angle)

    def animate(self):
        self.x += math.cos(math.radians(self.angle)) * self.velocity
        self.y += math.sin(math.radians(self.angle)) * self.velocity

class Sugar(Model):
    def __init__(self,world,x,y):
        super().__init__(world, x, y, 0)
        self.full_health = 40
        self.health = self.full_health

class Listenner :
    def __init__(self) :
        self.__handlers = []

    def add(self,handler) :
        self.__handlers.append(handler)

    def notify(self, *args, **keywargs) :
        for handler in self.__handlers :
            handler(*args, **keywargs)
