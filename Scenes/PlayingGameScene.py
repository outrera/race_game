import random

import pygame
from NPCCar import NPCCar
from Scenes import Scene
from Shared import GameConstants


class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)
        self.__numberOfPoliceCars = 0

    def update(self):
        super(PlayingGameScene, self).update()

        game = self.getGame()

        if game.getLives() <= 0:
            # game.playSound(GameConstants.SOUND_GAMEOVER)
            game.changeScene(GameConstants.GAMEOVER_SCENE)

        game.increaseScore(0.01)
        # level = game.getLevel()
        game.getBackground().update()
        car = game.getCar()
        car.update()
        npcCars = game.getNpcCars()

        npcCars[:] = [tup for tup in npcCars if self.isOnScreen(tup)]  # remove all none visible cars

        for npcCar in npcCars:
            npcCar.update()

        for npcCar in npcCars:
            if car.intersects(npcCar):
                # TODO: add crash sound
                # game.playSound(car.getHitSound())
                game.reduceLives()
                car.hit()

        self.addCar()

        # mouse_pos = pygame.mouse.get_pos()
        # car.setPosition((mouse_pos[0], car.getPosition()[1]))

    def render(self):
        game = self.getGame()
        background = game.getBackground()

        game.screen.blit(background.getSprite(), background.getPosition())
        game.screen.blit(background.getSprite(), background.getPosition2())

        npcCars = game.getNpcCars()
        for NPCCar in npcCars:
            if self.isOnScreen(NPCCar):
                game.screen.blit(NPCCar.getSprite(), NPCCar.getPosition())

        car = game.getCar()
        if car.toRender():
            game.screen.blit(car.getSprite(), car.getPosition())

        self.clearText()
        self.addText("Score: " + str(int(game.getScore())), x=0, y=0, size=50)
        self.addText("Lives: " + str(int(game.getLives())), x=0, y=30, size=50)
        self.addText("FPS: " + str(int(game.getFPS())), x=0, y=GameConstants.SCREEN_SIZE[1] - 30, size=30)

        super(PlayingGameScene, self).render()
        return

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        game = self.getGame()

        background = game.getBackground()
        car = game.getCar()

        speedx = car.getSpeed()[0]
        speedy = car.getSpeed()[1]

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speedx = -1 * GameConstants.CAR_SPEED[0]
                if event.key == pygame.K_RIGHT:
                    speedx = GameConstants.CAR_SPEED[0]
                # if event.key == pygame.K_UP:
                #     speedy += GameConstants.CAR_SPEED[1]
                #     if speedy >= GameConstants.CAR_SPEED[1]:
                #         speedy = GameConstants.CAR_SPEED[1]
                # if event.key == pygame.K_DOWN:
                #     speedy -= GameConstants.CAR_SPEED[1]
                #     if speedy < 0:
                #         speedy = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    speedx = 0
                # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                #     speedy = 0

        background.setSpeed((0, speedy))
        car.setSpeed((speedx, speedy))
        return

    def addCar(self):
        npcCars = self.getGame().getNpcCars()

        if len(npcCars) >= 8:
            return

        transform = random.getrandbits(1)  # if 1 car drives down, else car drives up

        rnd_sprite = random.choice([GameConstants.SPRITE_CAR_BLACK1,
                                    GameConstants.SPRITE_CAR_POLICE1,
                                    GameConstants.SPRITE_CAR_POLICE2,
                                    GameConstants.SPRITE_CAR_POLICE3,
                                    GameConstants.SPRITE_CAR_TAXI1,
                                    GameConstants.SPRITE_CAR_WHITE1,
                                    GameConstants.SPRITE_CAR_WHITE2,
                                    GameConstants.SPRITE_CAR_WHITE3,
                                    GameConstants.SPRITE_CAR_WHITE4,
                                    GameConstants.SPRITE_TRUCK_RED1])
        if "police" in rnd_sprite:
            if self.__numberOfPoliceCars > 1:
                return
            else:
                isPolice = True
        else:
            isPolice = False

        sprite = pygame.image.load(rnd_sprite)

        if transform:
            # place car in right lanes, facing down
            sprite = pygame.transform.flip(sprite, True, True)
            # positionx = random.choice([200, 300]) + GameConstants.CAR_SIZE[0] / 4
            positionx = random.choice([GameConstants.LANE0_X, GameConstants.LANE1_X])
            speed = (0, GameConstants.CAR_SPEED_NPC[1])

        else:
            # place car in left lan
            # positionx = random.choice([400, 500]) + GameConstants.CAR_SIZE[0] / 4
            positionx = random.choice([GameConstants.LANE2_X, GameConstants.LANE3_X])
            speed = (0, GameConstants.CAR_SPEED_NPC[1]/2)

        position = (positionx, -GameConstants.CAR_SIZE[1])  # y position is out of screen
        # position = (positionx, 1)  # y position is out of screen

        for npcCar in npcCars:
            if abs(npcCar.getPosition()[0] - positionx) < 200 and abs(npcCar.getPosition()[1] - position[1]) < 2.5 * GameConstants.CAR_SIZE[1]:
                return

        npcCars.append(NPCCar(position, sprite, speed))
        if isPolice:
            self.__numberOfPoliceCars += 1

        print("NPC Cars: {}".format(len(npcCars)))

    def isOnScreen(self, car):
        position = car.getPosition()

        if position[1] > GameConstants.SCREEN_SIZE[1] or position[1] < -GameConstants.CAR_SIZE[1] * 10:
            return False

        return True
