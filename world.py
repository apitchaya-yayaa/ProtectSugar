from models import *
from sound import Sound
from random import random
from random import randint
from time import time

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sugar = Sugar(self,width/2,height/2)
        self.ants = []
        self.ant_listenner = Listenner()
        self.start_game_time = time()
        self.prob = 0.001
        self.time_stamp = 0

    def animate(self, delta):
        for ant in self.ants:
            ant.animate()
        self.random_ant(time())
        # print(time())

    def update(self):
        for ant in self.ants :
            if ant.x < 0 or ant.x > self.width or ant.y < 0 or ant.y > self.height :
                self.ants.remove(ant)
                self.ant_listenner.notify('remove', ant)


    def create_ant(self, x, y) :
        ant = Ant(self,x,y)
        self.ants.append(ant)
        self.ant_listenner.notify('create' ,ant)

    def random_ant(self,time) :
        if (int(time - self.start_game_time) / 10) > self.time_stamp :
            self.time_stamp = (time - self.start_game_time) / 10
            self.prob += 0.0003

        if(float(randint(0,100))/100 <= self.prob) :
            x = 0
            y = 0
            if randint(0,1) == 0 :
                if randint(0,1) == 0 :
                    x = self.width
                y = randint(0,self.height)
            else :
                if randint(0,1) == 0 :
                    y = self.height
                x = randint(0,self.width)
            self.create_ant(x,y)

    def on_key_press(self, key, key_modifiers):
        self.key_list.append(key)

    def on_key_release(self, key, key_modifiers):
        try:
            self.key_list.remove(key)
        except:
            pass
