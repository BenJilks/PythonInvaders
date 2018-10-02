#!/bin/python
from Window import Window
from random import randint
from GameObjects import Player, ParrotHandler

WIDTH = 400/2
HEIGHT = 400/2

def main():
    window = Window(WIDTH, HEIGHT, "Python Invaders")
    renderer = window.renderer

    # Load sprites
    player_sprite = renderer.LoadSprite("Sprites/player.png")
    parrot_sprite = renderer.LoadSprite("Sprites/parrot.png")

    # Load objects
    player = Player(player_sprite, WIDTH, HEIGHT)
    parrots = ParrotHandler(parrot_sprite, WIDTH, HEIGHT)
    window.AddObject(player)
    window.AddObject(parrots)

    bullets = []
    while window.IsRunning():
        if player.ShouldFire():
            bullets.append([player.pos[0], player.pos[1]])
        
        bullets_hit = []
        for bullet in bullets:
            bullet[1] -= 10
            if parrots.TestCollision(bullet[0], bullet[1]) or bullet[1] <= 0:
                bullets_hit.append(bullet)
            else:
                renderer.SetPixel(int(bullet[0]), int(bullet[1]), 0, 255, 0)
        
        for bullet in bullets_hit:
            bullets.remove(bullet)
        window.Update()

if __name__ == '__main__':
    main()
