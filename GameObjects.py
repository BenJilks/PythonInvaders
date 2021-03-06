import numpy as np
from sdl2 import *
import Config as cf
import math

# Base class for all game objects, contains a position
class GameObject:
    def __init__(self, x, y):
        self.pos = np.array([x, y])
    
    def Render(self, renderer): pass
    def Update(self, delta): pass
    def OnEvent(self, event): pass

# Define player move directions
DIR_LEFT = 0
DIR_RIGHT = 1
DIR_STOP = -1

# The players object
class Player(GameObject):
    def __init__(self, sprite, width, height):
        super().__init__(width/2, height - 50)
        self.__sprite = sprite
        self.__dir = DIR_STOP
        self.__should_fire = False
        self.__moveKeyDown = None
    
    def Render(self, renderer):
        renderer.DrawSprite(self.__sprite, self.pos)
    
    def Update(self, delta):
        if self.__dir == DIR_LEFT:
            self.pos[0] -= cf.PLAYER_SPEED * delta
        elif self.__dir == DIR_RIGHT:
            self.pos[0] += cf.PLAYER_SPEED * delta

    def OnEvent(self, event):
        key = event.key.keysym.sym
        if event.type == SDL_KEYDOWN:
            # Set the move direction based on the key pressed
            if key == cf.KEY_LEFT:
                self.__moveKeyDown = key
                self.__dir = DIR_LEFT
            elif key == cf.KEY_RIGHT:
                self.__moveKeyDown = key
                self.__dir = DIR_RIGHT
            elif key == cf.KEY_FIRE:
                self.__should_fire = True

        elif event.type == SDL_KEYUP:
            if key == self.__moveKeyDown and key in cf.MOVEMENT_KEYS:
                self.__dir = DIR_STOP
        

    def ShouldFire(self):
        if self.__should_fire:
            self.__should_fire = False
            return True
        return False

MAX_OFFSET = 20
APPROACH_RATE = 0.7

# Parrot - enemy object
class Parrot(GameObject):
    def __init__(self, sprite, x, y):
        super().__init__(x, y)
        self.__sprite = sprite
    
    def Render(self, renderer, offset):
        pos = self.pos + offset
        renderer.DrawSprite(self.__sprite, pos)
    
    def TestCollision(self, bullet_x, bullet_y):
        if bullet_x > self.pos[0] and bullet_x < self.pos[0] + 20 and \
            bullet_y > self.pos[1] and bullet_y < self.pos[1] + 20:
            return True
        return False

# Handles all parrots in scene
class ParrotHandler(GameObject):
    def __init__(self, sprite, width, height):
        super().__init__(0, 0)
        self.__tick = 0
        self.__offset_x = 0
        self.__offset_y = 0

        # Create parrots in a grid
        self.__parrots = []
        
        p_width = 30 * 5
        start = width / 2 - p_width/2
        for i in range(5):
            for j in range(4):
                parrot = Parrot(sprite, start + i * 30, 10 + j * 30)
                self.__parrots.append(parrot)
    
    def Render(self, renderer):
        # Draw all parrots with current offset
        offset = np.array([self.__offset_x, self.__offset_y])
        for parrot in self.__parrots:
            parrot.Render(renderer, offset)
    
    def Update(self, delta):
        # Update position offsets
        self.__tick += delta * 0.05
        self.__offset_x = math.sin(self.__tick) * MAX_OFFSET
        self.__offset_y = self.__tick / APPROACH_RATE

    def TestCollision(self, bullet_x, bullet_y):
        should_delete = []

        for parrot in self.__parrots:
            if (parrot.TestCollision(bullet_x, bullet_y)):
                should_delete.append(parrot)
        
        for parrot in should_delete:
            self.__parrots.remove(parrot)
        return len(should_delete) > 0
