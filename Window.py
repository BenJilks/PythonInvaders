from sdl2 import *
from Renderer import Renderer
import ctypes
import Config as cf

class Window:
    def __init__(self, width, height, title):
        self.__width = width
        self.__height = height
        self.__title = title
        self.__should_close = False
        self.__objects = []

        # Init SDL, create window and renderer
        SDL_Init(SDL_INIT_EVERYTHING)
        self.__window = SDL_CreateWindow(
            title.encode("ASCII"), 
            SDL_WINDOWPOS_CENTERED,
            SDL_WINDOWPOS_CENTERED, 
            width * cf.SCALE,
            height * cf.SCALE, 0
        )
        self.renderer = Renderer(self.__width, self.__height, self.__window) 

    def AddObject(self, obj):
        self.__objects.append(obj)

    def Update(self):
        # Handle SDL events
        event = SDL_Event()
        while SDL_PollEvent(event):
            for obj in self.__objects:
                obj.OnEvent(event)
            
            if event.type == SDL_QUIT:
                self.Close()
        
        # Update screen
        for obj in self.__objects:
            obj.Update(0.1)
            obj.Render(self.renderer)
        self.renderer.Update()
    
    def IsRunning(self):
        return not self.__should_close

    def Close(self):
        self.__should_close = True
        SDL_DestroyWindow(self.__window)
