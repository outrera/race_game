import pygame


class GameObject:

    def __init__(self, position, size, sprite):
        self.__position = position
        self.__size = size
        self.__sprite = pygame.transform.smoothscale(sprite, (size[0], size[1]))

    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def getSize(self):
        return self.__size

    def getSprite(self):
        return self.__sprite

    def getRect(self):
        return pygame.Rect(self.getPosition(), self.getSize())

    def __intersectsY(self, other):
        otherPosition = other.getPosition()
        otherSize = other.getSize()

        if otherPosition[1] <= self.__position[1] <= otherPosition[1] + otherSize[1]:
            return True
        if otherPosition[1] < (self.__position[1] + self.__size[1]) <= (
                otherPosition[1] + otherSize[1]):
            return True
        return False

    def __intersectsX(self, other):
        otherPosition = other.getPosition()
        otherSize = other.getSize()

        if otherPosition[0] <= self.__position[0] <= otherPosition[0] + otherSize[0]:
            return True
        if otherPosition[0] < (self.__position[0] + self.__size[0]) <= (
                otherPosition[0] + otherSize[0]):
            return True
        return False

    def intersects(self, other):
        if self.__intersectsY(other) and self.__intersectsX(other):
            return True
        else:
            return False