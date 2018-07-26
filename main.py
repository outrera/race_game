import pygame
from Shared.GameConstants import GameConstants
from Levels.Level import Level
from Car import Car
from Background import Background
from Scenes import *


class Race:

    def __init__(self):
        self.__lives = 3
        self.__score = 0

        # self.__level = Level(self)  # create a new level pass the game to it
        self.__car = Car((GameConstants.LANE2_X,
                          # GameConstants.SCREEN_SIZE[1] - GameConstants.CAR_SIZE[1]),
                          GameConstants.SCREEN_SIZE[1]/2),
                         pygame.image.load(GameConstants.SPRITE_CAR))
        self.__npcCars = []
        self.__background = Background(pygame.image.load(GameConstants.SPRITE_BACKGROUND))

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Racing Game")

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE,
                                              pygame.DOUBLEBUF, 32)

        pygame.mouse.set_visible(0)

        self.__scenes = (
            PlayingGameScene(self),
            GameOverScene(self),
            HighScoreScene(self),
            MenuScene(self)
        )

        self.__currentScene = 0

        self.__sounds = ()

    def start(self):
        while True:
            self.__clock.tick(GameConstants.FPS)

            self.screen.fill((0, 0, 0))  # TODO: change this background

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.update()
            currentScene.render()

            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene

    def getFPS(self):
        return self.__clock.get_fps()

    # def getLevel(self):
    #     return self.__level

    def getScore(self):
        return self.__score

    def increaseScore(self, score):
        self.__score += score

    def getLives(self):
        return self.__lives

    def increaseLives(self):
        self.__lives += 1

    def reduceLives(self):
        self.__lives -= 1

    def getCar(self):
        return self.__car

    def getNpcCars(self):
        return self.__npcCars

    def getBackground(self):
        return self.__background

    def playsound(self, soundClip):
        sound = self.__sounds[soundClip]
        sound.stop()
        sound.play()

    def reset(self):
        # resets the game to it's original state
        self.__lives = 3
        self.__score = 0
        self.__car = Car((GameConstants.LANE2_X,
                          # GameConstants.SCREEN_SIZE[1] - GameConstants.CAR_SIZE[1]),
                          GameConstants.SCREEN_SIZE[1]/2),
                         pygame.image.load(GameConstants.SPRITE_CAR))
        self.__npcCars = []  # clear all cars from screen


Race().start()
