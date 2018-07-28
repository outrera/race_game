import pygame

from HighScore import HighScore
from Scenes import Scene
from Shared import GameConstants


class HighScoreScene(Scene):

    def __init__(self, game):
        super(HighScoreScene, self).__init__(game)
        # sprite = pygame.image.load(GameConstants.SPRITE_HIGH_SCORE)
        # self.__highScoreSprite = pygame.transform.smoothscale(sprite,
        #                                                       (int(GameConstants.SCREEN_SIZE[0]/4),
        #                                                        int(GameConstants.SCREEN_SIZE[1]/4)))
        self.__highScoreSprite = pygame.image.load(GameConstants.SPRITE_HIGH_SCORE).convert_alpha()

    def render(self):
        self.getGame().screen.blit(self.__highScoreSprite, (50, 50))
        self.clearText()

        highscore = HighScore()

        x = 350
        y = 100

        for score in highscore.getScores():
            self.addText(score[0], x, y, size=30)  # print the player name
            self.addText(str(score[1]), x+200, y, size=30)  # print the player score
            y += 30

        self.addText("Press F1 to start a new game", x, y+60, size=30)

        super(HighScoreScene, self).render()

    def handleEvents(self, events):
        super(HighScoreScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.getGame().reset()
                    self.getGame().changeScene(GameConstants.PLAYING_SCENE)
