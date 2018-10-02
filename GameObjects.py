import numpy as np
from sdl2 import *
import Config as cf
import math

# Base class for all game objects, contains a position
class GameObject:
    def __init__(self, x, y):
        self._pos = np.array([x, y])
    
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
        super().__init__(width/2 - 5, height - 50)
        self.__sprite = sprite
        self.__dir = DIR_STOP
    
    def Render(self, renderer):
        renderer.DrawSprite(self.__sprite, self._pos)
    
    def Update(self, delta):
        if self.__dir == DIR_LEFT:
            self._pos[0] += cf.PLAYER_SPEED * delta
        elif self.__dir == DIR_RIGHT:
            self._pos[0] -= cf.PLAYER_SPEED * delta
    
    def OnEvent(self, event):
        key = event.key.keysys.sym
        if event.type == SDL_KEYDOWN:
            # Set the move direction based on the key pressed
            if key == cf.KEY_LEFT:
                self.__dir = DIR_LEFT
            elif key == cf.KEY_RIGHT:
                self.__dir = DIR_RIGHT

        elif event.type == SDL_KEYUP:
            # If a movement key is released, then stop movement
            if key in cf.MOVEMENT_KEYS:
                self._dir == DIR_STOP

MAX_OFFSET = 20
APPROACH_RATE = 20

# Parot, enmie object
class Parrot(GameObject):
    def __init__(self, sprite, x, y):
        super().__init__(x, y)
        self.__sprite = sprite
    
    def Render(self, renderer, offset):
        pos = self._pos + offset
        renderer.DrawSprite(self.__sprite, self._pos)

# Handles all parrots in scene
class ParrotHandler(GameObject):
    def __init__(self, sprite, width, height):
        super().__init__(0, 0)
        self.__tick = 0
        self.__offset_x = 0
        self.__offset_y = 0

        # Create parrots in a grid
        self.__parrots = []
        for i in range(5):
            parrot = Parrot(sprite, i * 30, 0)
            self.__parrots.append(parrot)
    
    def Render(self, renderer):
        # Draw all parrots with current offset
        offset = np.array([self.__offset_x, self.__offset_y])
        for parrot in self.__parrots:
            parrot.Render(renderer, offset)
    
    def Update(self, delta):
        # Update position offsets
        self.__tick += delta
        self.__offset_x = math.sin(self.__tick) * MAX_OFFSET
        self.__offset_y = self.__tick / APPROACH_RATE
