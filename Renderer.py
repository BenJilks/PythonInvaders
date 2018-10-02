from sdl2 import *
import ctypes
import Config as cf
from PIL import Image

class Sprite:
    def __init__(self, width, height, img):
        ##self.pixels = pixels ##Pointless for now
        self.width = width
        self.height = height
        self.img = img

##Handles drawing to pixel array
class Renderer:
    def __init__(self, width, height, sdlWindow):
        ##SDL2 renderer and texture (OpenGL graphics)
        self.__width = width
        self.__height = height
        self.__renderer = SDL_CreateRenderer(
            sdlWindow, -1, 
            SDL_RENDERER_ACCELERATED, 
            SDL_RENDERER_PRESENTVSYNC
        )

        self.__texture = SDL_CreateTexture(
            self.__renderer, 
            SDL_PIXELFORMAT_RGB888,
            SDL_TEXTUREACCESS_STREAMING, 
            int(width), int(height)
        )

        ##Set Default Renderer Colour
        SDL_SetRenderDrawColor(self.__renderer,0,0,0,255)
        self.__size = int(width * height * 4)
        self.__pixels = (ctypes.c_char * self.__size)()

    # Load an image into and array of pixels and returns sprite
    def LoadSprite(self, file_path):
        img = Image.open(file_path)

        ##Convert image to usable form
        im = img.convert("RGBA")
        return Sprite(img.width, img.height, img)

    # Draw a sprite at position
    def DrawSprite(self, sprite, pos):
        xmin = pos[0]
        ymin = pos[1]
        xmax = xmin + sprite.width
        ymax = ymin + sprite.height

        xtemp = 0
        ytemp = 0

        for i in range(int(ymin),int(ymax)-1):
            xtemp = 0
            for j in range(int(xmin), int(xmax)):
                r,g,b,a = sprite.img.getpixel((xtemp, ytemp))
                if a > 0:
                    self.SetPixel(j, i, r, g, b)
                xtemp += 1
            ytemp += 1

    def Prepare(self):
        ctypes.memset(self.__pixels, 0, self.__size)

    def Update(self):
        # Update screen
        SDL_UpdateTexture(
            self.__texture, 
            None, 
            self.__pixels,
            ctypes.c_int(int(self.__width * 4))
        )
        SDL_RenderCopy(
            self.__renderer, 
            self.__texture,
            None,
            None
        )

        SDL_RenderPresent(self.__renderer)
        ##SDL_Delay(1)
        ##Clear the screen
        SDL_RenderClear(self.__renderer) 
        self.Prepare()

    def SetPixel(self, x, y, r, g, b):
        index = int((x*4) + (y*self.__width*4))
        self.__pixels[index] = ctypes.c_char(r)
        self.__pixels[index+1] = ctypes.c_char(g)
        self.__pixels[index+2] = ctypes.c_char(b)
