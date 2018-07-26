import os


class Level:

    def __init__(self, game):
        self.__game = game
        self.__cars = []
        self.__currentLevel = 0

    def loadNextLevel(self):
        self.__currentLevel += 1
        filename = os.path.join("Assets", "Levels", "Level"+str(self.__currentLevel))

        if not os.path.exists(filename):
            self.loadRandom()
        else:
            self.load(self.__currentLevel)

    def loadRandom(self):
        pass

    def load(self, level):
        self.__currentLevel = level
        pass
