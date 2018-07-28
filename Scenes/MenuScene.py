import pygame
from Scenes import Scene
from Shared.GameConstants import GameConstants


class MenuScene(Scene):

    def __init__(self, game):
        super(MenuScene, self).__init__(game)

        self.addText("F1 - Start Game", x=300, y=400, size=30)
        self.addText("F2 - High Scores", x=300, y=440, size=30)
        self.addText("F3 - Quit", x=300, y=480, size=30)

        sprite = pygame.image.load(GameConstants.SPRITE_MENU).convert_alpha()
        self.__menuSprite = pygame.transform.smoothscale(sprite, GameConstants.SCREEN_SIZE)

    def render(self):
        self.getGame().screen.blit(self.__menuSprite, (0, 0))
        super(MenuScene, self).render()

    def handleEvents(self, events):
        super(MenuScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_F1:
                    self.getGame().changeScene(GameConstants.PLAYING_SCENE)
                if event.key == pygame.K_F2:
                    self.getGame().changeScene(GameConstants.HIGHSCORE_SCENE)
                if event.key == pygame.K_F3:
                    exit()
