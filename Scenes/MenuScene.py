# import pygame
from Scenes import Scene


class MenuScene(Scene):

    def __init__(self, game):
        super(MenuScene, self).__init__(game)

    def update(self):
        super(MenuScene, self).update()

        game = self.getGame()
        # level = game.getLevel()

    def render(self):
        super(MenuScene, self).render()

    def handleEvents(self, event):
        super(MenuScene, self).handleEvents(event)
