from Shared import *


class NPCCar(GameObject):

    def __init__(self, position, sprite, size, speed):
        super(NPCCar, self).__init__(position, size, sprite)
        self.__speed = (0, speed[1])

    def update(self):
        position = self.getPosition()
        newPosition = (position[0], position[1] + self.getSpeed()[1])
        self.setPosition(newPosition)

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed


