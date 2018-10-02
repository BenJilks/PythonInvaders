#!/bin/python
from Window import Window
from random import randint

def main():
    window = Window(80, 60, "Python Invaders")
    renderer = window.renderer

    while window.IsRunning():
        for i in range(0, 80):
            for j in range(0, 60):
                if randint(0, 200) == 0:
                    renderer.SetPixel(i, j, randint(0, 255), 
                        randint(0, 255), randint(0, 255))
        window.Update()

if __name__ == '__main__':
    main()
