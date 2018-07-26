import pygame

from HighScore import HighScore
from Scenes import Scene
from Shared.GameConstants import GameConstants


class GameOverScene(Scene):

    def __init__(self, game):
        super(GameOverScene, self).__init__(game)
        self.__playerName = ""
        sprite = pygame.image.load(GameConstants.SPRITE_CAR_CRASH)
        self.__carCrashSprite = pygame.transform.smoothscale(sprite,
                                                             (int(GameConstants.SCREEN_SIZE[0] / 4),
                                                              int(GameConstants.SCREEN_SIZE[1] / 4)))

    def update(self):
        super(GameOverScene, self).update()

    def render(self):
        self.getGame().screen.blit(self.__carCrashSprite, (50, 50))
        self.clearText()
        self.addText("Press F1 to restart the game", 400, 400, size=30)
        self.addText("Enter Player Name: ", 420, 200 - 30, size=30)
        self.addText(self.__playerName, 420, 200, size=30)
        super(GameOverScene, self).render()

    def handleEvents(self, events):
        super(GameOverScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = self.getGame()
                    HighScore().add(self.__playerName, int(self.getGame().getScore()))
                    game.reset()
                    game.changeScene(GameConstants.HIGHSCORE_SCENE)
                elif 65 <= event.key <= 122:  # limit to a-z characters
                    self.__playerName += chr(event.key)

                if event.key == pygame.K_F1:
                    self.getGame().reset()
                    self.getGame().changeScene(GameConstants.PLAYING_SCENE)
