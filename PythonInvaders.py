#!/bin/python
from Window import Window
from random import randint

def main():
    window = Window(400, 400, "Python Invaders")
    renderer = window.renderer

    while window.IsRunning():
        renderer.FillColour(255)
        window.Update()

if __name__ == '__main__':
    main()
