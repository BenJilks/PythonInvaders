#!/bin/python
from Window import Window
from random import randint
from GameObjects import Player, ParrotHandler

WIDTH = 400
HEIGHT = 400

def main():
    print("here")
    window = Window(WIDTH, HEIGHT, "Python Invaders")
    renderer = window.renderer

    # Load sprites
    player_sprite = renderer.LoadSprite("Sprites/player.png")
    parrot_sprite = renderer.LoadSprite("Sprites/parrot.png")

    # Load objects
    player = Player(player_sprite, WIDTH, HEIGHT)
    parrots = ParrotHandler(parrot_sprite, WIDTH, HEIGHT)
    objects = [player, parrots]

    while window.IsRunning():
        # Do better
        for obj in objects:
            obj.Render(renderer)
            obj.Update(0.1)
        
        window.Update()

if __name__ == '__main__':
    main()