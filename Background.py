from Shared import GameObject, GameConstants


class Background(GameObject):

    def __init__(self, sprite):
        super(Background, self).__init__((0, 0), GameConstants.SCREEN_SIZE, sprite)
        self.__speedy = 0

    def update(self):
        position = self.getPosition()
        positionY = position[1] + self.getSpeed()[1]
        if positionY == GameConstants.SCREEN_SIZE[1]:
            positionY = 0
        newPosition = (0, positionY)
        self.setPosition(newPosition)

    def getSpeed(self):
        return self.__speedy

    def setSpeed(self, speedy):
        self.__speedy = speedy

    def getPosition2(self):
        # returns the position of the second background sprite to create the effect of sliding background
        position = self.getPosition()
        newPosition = (position[0], position[1] - self.getSize()[1])
        return newPosition

