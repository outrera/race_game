import pygame


class Scene:

    def __init__(self, game):
        self.__game = game
        self.__texts = []  # an empty list of texts to print

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                exit()

    def clear(self):
        pass

    def update(self):
        pass

    def render(self):
        for text in self.__texts:
            self.__game.screen.blit(text[0], text[1])

    def addText(self, string, x=0, y=0, color=[255, 255, 255], background=None, size=17):
        # def addText(self, string, x=0, y=0, color=[255, 255, 255], background=[0, 0, 0], size=17):
        font = pygame.font.Font(None, size)
        self.__texts.append([font.render(string, True, color, background), (x, y)])

    def clearText(self):
        self.__texts = []

    def getGame(self):
        return self.__game
