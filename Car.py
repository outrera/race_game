from Shared import *


class Car(GameObject):

    def __init__(self, position, sprite):
        super(Car, self).__init__(position, GameConstants.CAR_SIZE, sprite)
        self.__speed = (0, GameConstants.CAR_SPEED[1])
        self.__blinkingCounter = 0
        self.__render = True

    def update(self):
        if self.__blinkingCounter > 0:
            # decrement blink counter to reset it
            self.__blinkingCounter -= 1

        position = self.getPosition()
        newPosition = (position[0] + self.getSpeed()[0], position[1])
        self.setPosition(newPosition)

    def setPosition(self, position):
        newPosition = [position[0], position[1]]
        size = self.getSize()

        # limit the xPosition to screen borders
        if newPosition[0] + size[0] > GameConstants.SCREEN_SIZE[0]:
            newPosition[0] = GameConstants.SCREEN_SIZE[0] - size[0]
        if newPosition[0] < 0:
            newPosition[0] = 0

        super(Car, self).setPosition(newPosition)

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed
    
    def intersects(self, other):
        if self.__blinkingCounter > 0:
            return False
        return super(Car, self).intersects(other)
    
    def hit(self):
        # when the car is hit it blinks
        self.__blinkingCounter = GameConstants.FPS * 3  # number of frames in 3 seconds
        return

    def toRender(self):
        # I want it to blink every half a second, unless counter is zeroed
        if self.__blinkingCounter == 0:
            return True
        div = int(self.__blinkingCounter/(GameConstants.FPS/4))
        if div % 2 == 0:
            return True
        else:
            return False

