import pygame

from Shared import GameObject, GameConstants


class RoadMarking(GameObject):

    def __init__(self, sprite):
        positionx = GameConstants.SCREEN_SIZE[0]/2 - GameConstants.LANE_SIZE
        sizex = int(5*GameConstants.SCREEN_SIZE[0]/800)
        super(RoadMarking, self).__init__((positionx, 0), (sizex, GameConstants.SCREEN_SIZE[1]), sprite)
        self.__speedy = 0

    def update(self):
        position = self.getPosition()
        positionY = position[1] + self.getSpeed()[1]
        if positionY == GameConstants.SCREEN_SIZE[1]:
            positionY = 0
        newPosition = (position[0], positionY)
        self.setPosition(newPosition)

    def getSpeed(self):
        return self.__speedy

    def setSpeed(self, speedy):
        self.__speedy = speedy

    def getPositionLeftLane(self):
        return self.getPosition()

    def getPositionLeftLaneUpper(self):
        # returns the position of the second background sprite to create the effect of sliding background
        position = self.getPosition()
        newPosition = (position[0], position[1] - self.getSize()[1])
        return newPosition

    def getPositionRightLane(self):
        position = self.getPositionLeftLane()
        newPosition = (position[0] + 2 * GameConstants.LANE_SIZE, position[1])
        return newPosition

    def getPositionRightLaneUpper(self):
        position = self.getPositionRightLane()
        newPosition = (position[0], position[1] - self.getSize()[1])
        return newPosition

    def getRectLeft(self):
        return self.getRect()

    def getRectLeftUpper(self):
        return pygame.Rect(self.getPositionLeftLaneUpper(), self.getSize())

    def getRectRight(self):
        return pygame.Rect(self.getPositionRightLane(), self.getSize())

    def getRectRightUpper(self):
        return pygame.Rect(self.getPositionRightLaneUpper(), self.getSize())