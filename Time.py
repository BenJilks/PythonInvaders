import time

class Time:
    def __init__(self):
        self.fps = 0
        self.framesRendered = 0
        self.startTime = time.time()
        self.deltaTime = 0
        self.passedTime = 0
        self.__startTime = 0
        self.__endTime = 0

    def Start(self):
        self.__startTime = time.time()

    def Stop(self):
        self.__endTime = time.time()
        self.deltaTime = self.__endTime-self.__startTime