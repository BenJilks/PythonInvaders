import numpy as np
from sdl2 import *
import Config as cf

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
        super().__init__(width / 2 - 5, height - 15)
        self.__sprite = sprite
        self.__dir = DIR_STOP
    
    def Render(self, renderer):
        renderer.DrawSprite(self.__sprite, self._pos)
    
    def Update(self, delta):
        if self.__dir == DIR_LEFT:
            self._pos[0] += cf.PLAYER_SPEED * delta
        elif self.__dir = DIR_RIGHT:
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
