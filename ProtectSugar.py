import arcade
from time import time
from world import World
import pyglet.gl as gl

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

    def draw(self):
        self.sync_with_model()
        super().draw()

class ProtectSugarGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width
        self.height = height
        arcade.set_background_color(arcade.color.WHITE)
        self.world = World(width,height)
        self.ant_sprites = []
        self.hand1 = arcade.Sprite("images/hand.png")
        self.hand2 = arcade.Sprite("images/hand1.png")
        self.hand = self.hand1
        self.world.ant_listenner.add(self.ant_listenner_notify)
        self.bg = arcade.Sprite("images/bg.png")
        self.bg.set_position(width/2,height/2)
        self.gameover = arcade.Sprite("images/gameover.png")
        self.gameover.set_position(width/2,height/2)
        self.sugar_sprite1 = ModelSprite("images/sugar.png",model=self.world.sugar)
        self.sugar_sprite2 = ModelSprite("images/sugar less1.png",model=self.world.sugar)
        self.sugar_sprite3 = ModelSprite("images/sugar less2.png",model=self.world.sugar)
        self.sugar_sprite4 = ModelSprite("images/sugar less3.png",model=self.world.sugar)
        self.sugar_sprite5 = ModelSprite("images/sugar less4.png",model=self.world.sugar)
        self.sugar_sprite6 = ModelSprite("images/sugar less5.png",model=self.world.sugar)
        self.sugar_sprite7 = ModelSprite("images/blank.png",model=self.world.sugar)
        self.sugar_sprite = self.sugar_sprite1

    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        if self.world.sugar.health > 0 :
            self.sugar_sprite.draw()
        if self.world.sugar.health == 0 :
            self.gameover.draw()
        for ant_sprite in self.ant_sprites :
            ant_sprite.draw()
        self.hand.draw()



    def on_mouse_press(self,x, y, button, modifiers) :
        self.hand = self.hand2
        for ant in self.world.ants :
            if(ant.x >= x-60 and ant.x <= x+40 and ant.y >= y-40 and ant.y <= y+34 ) :
                self.ant_listenner_notify('remove', ant)
                self.world.ants.remove(ant)

    def on_mouse_motion(self, x, y, dx, dy) :
        self.hand1.set_position(x+95,y-50)
        self.hand2.set_position(x+47,y-42)

    def on_mouse_release(self, x, y, button, modifiers):
        self.hand = self.hand1


    def ant_listenner_notify(self, message, ant) :
        if message == 'create' :
            self.ant_sprites.append(ModelSprite('images/ant1.png', model=ant))
        elif message == 'remove' :
            for ant_sprite in self.ant_sprites :
                if ant_sprite.model == ant :
                    self.ant_sprites.remove(ant_sprite)

    def animate(self, delta):
        self.world.animate(delta)
        self.world.update()
        for ant_sprite in self.ant_sprites :
            ant_sprite.sync_with_model()
        self.ant_hit_sugar()
        self.update_sugar()

    def ant_hit_sugar(self) :
        for ant_sprite in self.ant_sprites :
            # if(ant.x >= self.sugar.x-20 and ant.x <= self.sugar.x+40 and ant.y >= self.sugar.y and ant.y <= self.sugar.y+20 ) :
            #     if self.world.sugar.health > 0 :
            #         self.world.sugar.health -= 1
            #         self.ant_sprites.remove(ant_sprite)
            #         print(self.world.sugar.health)
            if arcade.check_for_collision(ant_sprite, self.sugar_sprite) :
                if self.world.sugar.health > 0 :
                    self.world.sugar.health -= 1
                    self.ant_sprites.remove(ant_sprite)
                    print(self.world.sugar.health)

    def update_sugar(self) :
        if self.world.sugar.health < 10 :
            self.sugar_sprite = self.sugar_sprite6
        elif self.world.sugar.health < 20 :
            self.sugar_sprite = self.sugar_sprite5
        elif self.world.sugar.health < 25 :
            self.sugar_sprite = self.sugar_sprite4
        elif self.world.sugar.health < 30 :
            self.sugar_sprite = self.sugar_sprite3
        elif self.world.sugar.health < 35 :
            self.sugar_sprite = self.sugar_sprite2
        elif self.world.sugar.health < 30:
            self.sugar_sprite = self.sugar_sprite1


    def on_key_press(self, key, key_modifiers):
        pass
    def on_key_release(self, key, key_modifiers):
        pass

if __name__ == '__main__':
    window = ProtectSugarGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
