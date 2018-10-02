from sdl2 import *
import ctypes
import Config as cf

class Sprite:
    def __init__(self, pixels, width, height):
        self.pixels = pixels
        self.width = width
        self.height = height

##Handles drawing to pixel array
class Renderer:
    def __init__(self, width, height, sdlWindow):
        ##SDL2 renderer and texture (OpenGL graphics)
        self.__width = width
        self.__height = height
        self.__renderer = SDL_CreateRenderer(sdlWindow, -1, SDL_RENDERER_ACCELERATED,SDL_RENDERER_PRESENTVSYNC)
        self.__texture = SDL_CreateTexture(self.__renderer, SDL_PIXELFORMAT_RGB888, SDL_TEXTUREACCESS_STREAMING, width, height)

        ##Set Default Renderer Colour
        SDL_SetRenderDrawColor(self.__renderer,0,0,0,255)
        self.__pixels = (ctypes.c_char * (width * height * 4))()

    # Load an image into and array of pixels and returns sprite
    def LoadSprite(self, file_path):
        pass

    # Draw a sprite at position
    def DrawSprite(self, sprite, pos):
        pass

    def Update(self):
        # Update screen
        SDL_UpdateTexture(
            self.__texture, 
            None, 
            self.__pixels,
            ctypes.c_int(self.__width * 4)
        )
        SDL_RenderCopy(
            self.__renderer, 
            self.__texture,
            None,
            None
        )
        SDL_RenderPresent(self.__renderer)
        ##SDL_Delay(0)
        SDL_RenderClear(self.__renderer) 

    def SetPixel(self, x, y, r, g, b):
        index = (x*4) + (y*self.__width*4)
        self.__pixels[index] = ctypes.c_char(r)
        self.__pixels[index+1] = ctypes.c_char(g)
        self.__pixels[index+2] = ctypes.c_char(b)