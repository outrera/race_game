import random

import pygame
from NPCVehicle import NPCCar
from Scenes import Scene
from Shared import GameConstants


def getObjectSize(string):
    if "bus" in string:
        return GameConstants.BUS_SIZE
    if "truck" in string:
        if "long" in string:
            return GameConstants.TRUCK_LONG_SIZE
        if "medium" in string:
            return GameConstants.TRUCK_MEDIUM_SIZE
    if "car" in string:
        return GameConstants.CAR_SIZE
    if "tree" in string:
        return GameConstants.TREE_SIZE
    if "bush" in string:
        return GameConstants.BUSH_SIZE
    if "house" in string:
        return random.choice(GameConstants.HOUSE_SIZE)


class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)
        self.__numberOfPoliceCars = 0
        background = pygame.image.load(GameConstants.SPRITE_BACKGROUND).convert_alpha()
        self.__background = pygame.transform.smoothscale(background, GameConstants.SCREEN_SIZE)
        game = self.getGame()
        game.screen.blit(self.__background, (0, 0))  # draw the background only once
        game.addDirtyRect(pygame.Rect((0, 0), GameConstants.SCREEN_SIZE))

    def clear(self):
        # TODO: add rectangles to game.__dirtyrects
        game = self.getGame()


        npcCars = game.getNpcCars()
        offRoadObjs = game.getOffRoadObstacles()

        # blit the background over the NPC cars
        for NPCCar in npcCars:
            if self.isOnScreen(NPCCar):
                pos = NPCCar.getPosition()
                rect = NPCCar.getRect()
                game.screen.blit(self.__background, dest=pos, area=rect)
                game.addDirtyRect(rect)

        # blit the background over the off road objects
        for offRoadObj in offRoadObjs:
            if self.isOnScreen(offRoadObj):
                pos = offRoadObj.getPosition()
                rect = offRoadObj.getRect()
                game.screen.blit(self.__background, dest=pos, area=rect)
                game.addDirtyRect(rect)

        # blit the bacgkround over the road markings
        roadMarking = game.getRoadSurfaceMarking()
        game.screen.blit(self.__background, dest=roadMarking.getPositionLeftLane(), area=roadMarking.getRect())
        game.screen.blit(self.__background, dest=roadMarking.getPositionLeftLaneUpper(),
                         area=roadMarking.getRectLeftUpper())
        game.screen.blit(self.__background, dest=roadMarking.getPositionRightLane(), area=roadMarking.getRectRight())
        game.screen.blit(self.__background, dest=roadMarking.getPositionRightLaneUpper(),
                         area=roadMarking.getRectRightUpper())

        game.addDirtyRect(roadMarking.getRectLeft())
        game.addDirtyRect(roadMarking.getRectLeftUpper())
        game.addDirtyRect(roadMarking.getRectRight())
        game.addDirtyRect(roadMarking.getRectRightUpper())

        car = game.getCar()
        pos = car.getPosition()
        rect = car.getRect()
        game.screen.blit(self.__background, dest=pos, area=rect)
        game.addDirtyRect(rect)

        self.clearText()

        return

    def update(self):
        super(PlayingGameScene, self).update()

        game = self.getGame()

        if game.getLives() <= 0:
            # game.playSound(GameConstants.SOUND_GAMEOVER)
            game.changeScene(GameConstants.GAMEOVER_SCENE)

        game.increaseScore(0.01)
        # level = game.getLevel()
        # game.getBackground().update()
        game.getRoadSurfaceMarking().update()

        car = game.getCar()
        car.update()
        npcCars = game.getNpcCars()
        offRoadObjs = game.getOffRoadObstacles()

        npcCars[:] = [tup for tup in npcCars if self.isOnScreen(tup)]  # remove all none visible cars
        offRoadObjs[:] = [tup for tup in offRoadObjs if self.isOnScreen(tup)]  # remove all none visible cars

        for npcCar in npcCars:
            npcCar.update()
            if car.intersects(npcCar):
                # TODO: add crash sound
                # game.playSound(car.getHitSound())
                game.reduceLives()
                car.hit()

        for offRoadObj in offRoadObjs:
            offRoadObj.update()
            if car.intersects(offRoadObj):
                # TODO: add crash sound
                game.reduceLives()
                car.hit()

        self.addNpcVehicles()
        self.addOffRoadObstacles()

        # mouse_pos = pygame.mouse.get_pos()
        # car.setPosition((mouse_pos[0], car.getPosition()[1]))

    def render(self):
        game = self.getGame()
        # background = game.getBackground()
        # game.screen.blit(background.getSprite(), background.getPosition())
        # game.screen.blit(background.getSprite(), background.getPosition2())

        npcCars = game.getNpcCars()
        offRoadObjs = game.getOffRoadObstacles()

        for NPCCar in npcCars:
            if self.isOnScreen(NPCCar):
                game.screen.blit(NPCCar.getSprite(), NPCCar.getPosition())
                game.addDirtyRect(NPCCar.getRect())

        for offRoadObj in offRoadObjs:
            if self.isOnScreen(offRoadObj):
                game.screen.blit(offRoadObj.getSprite(), offRoadObj.getPosition())
                game.addDirtyRect(offRoadObj.getRect())

        roadMarking = game.getRoadSurfaceMarking()
        # blit on left lane
        game.screen.blit(roadMarking.getSprite(), roadMarking.getPositionLeftLane())
        game.screen.blit(roadMarking.getSprite(), roadMarking.getPositionLeftLaneUpper())

        # blit of right lane
        game.screen.blit(roadMarking.getSprite(), roadMarking.getPositionRightLane())
        game.screen.blit(roadMarking.getSprite(), roadMarking.getPositionRightLaneUpper())

        # game.addDirtyRect(roadMarking.getRectLeft())
        game.addDirtyRect(roadMarking.getRectLeftUpper())
        game.addDirtyRect(roadMarking.getRectRight())
        game.addDirtyRect(roadMarking.getRectRightUpper())

        car = game.getCar()
        if car.toRender():
            game.screen.blit(car.getSprite(), car.getPosition())
            game.addDirtyRect(car.getRect())

        self.clearText()
        self.addText("Score: " + str(int(game.getScore())), x=0, y=0, size=50)
        self.addText("Lives: " + str(int(game.getLives())), x=0, y=30, size=50)
        self.addText("FPS: " + str(int(game.getFPS())), x=0, y=GameConstants.SCREEN_SIZE[1] - 30, size=30)

        super(PlayingGameScene, self).render()
        return

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        game = self.getGame()

        # background = game.getBackground()
        roadMarkings = game.getRoadSurfaceMarking()
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

        # background.setSpeed((0, speedy))
        roadMarkings.setSpeed((0, speedy))
        car.setSpeed((speedx, speedy))
        return

    def addNpcVehicles(self):
        npcCars = self.getGame().getNpcCars()

        if len(npcCars) >= 8:
            return

        transform = random.getrandbits(1)  # if 1 car drives down, else car drives up

        rnd_sprite_string = random.choice(list(GameConstants.VEHICLES.values()))

        if "police" in rnd_sprite_string:
            if self.__numberOfPoliceCars > 1:
                return
            else:
                isPolice = True
        else:
            isPolice = False

        sprite = pygame.image.load(rnd_sprite_string).convert_alpha()
        size = getObjectSize(rnd_sprite_string)

        if transform:
            # place car in left lanes, facing down
            sprite = pygame.transform.flip(sprite, True, True)
            positionx = random.choice([GameConstants.LANE0_X, GameConstants.LANE1_X])
            speed = (0, int(GameConstants.CAR_SPEED_NPC[1]*2))

        else:
            # place car in right lan
            positionx = random.choice([GameConstants.LANE2_X, GameConstants.LANE3_X])
            speed = (0, GameConstants.CAR_SPEED_NPC[1])

        position = (positionx, -size[1])  # y position is out of screen

        for npcCar in npcCars:
            conditionX = abs(npcCar.getPosition()[0] - positionx) < GameConstants.LANE_SIZE * 2
            conditionY = abs(npcCar.getPosition()[1] - position[1]) < 3 * max(size[1], GameConstants.CAR_SIZE[1])
            if conditionX and conditionY:
                return

        npcCars.append(NPCCar(position, sprite, size, speed))
        if isPolice:
            self.__numberOfPoliceCars += 1

        print("NPC Cars: {}".format(len(npcCars)))

    def addOffRoadObstacles(self):
        offRoadObstacles = self.getGame().getOffRoadObstacles()

        if len(offRoadObstacles) >= 16:
            return

        rnd_sprite_string = random.choice(list(GameConstants.OFF_ROAD_OBSTACLES.values()))

        sprite = pygame.image.load(rnd_sprite_string).convert_alpha()
        size = getObjectSize(rnd_sprite_string)

        left_grass = random.getrandbits(1)

        if left_grass:
            positionx = random.randint(0, int(GameConstants.LANE0_X - size[0]))
        else:
            positionx = random.randint(int(GameConstants.LANE3_X + GameConstants.LANE_SIZE),
                                       int(GameConstants.SCREEN_SIZE[0]-size[0]))

        position = (positionx, -size[1])  # y position is out of screen

        for obs in offRoadObstacles:
            conditionX = abs(obs.getPosition()[0] - positionx) < int(GameConstants.LANE_SIZE)
            conditionY = abs(obs.getPosition()[1] - position[1]) < 3 * max(size[1], GameConstants.CAR_SIZE[1])
            if conditionX and conditionY:
                return

        offRoadObstacles.append(NPCCar(position, sprite, size, (0, int(GameConstants.CAR_SPEED[1]))))

        print("Off Road obstacles: {}".format(len(offRoadObstacles)))

    def isOnScreen(self, car):
        position = car.getPosition()

        if position[1] > GameConstants.SCREEN_SIZE[1] or position[1] < -GameConstants.CAR_SIZE[1] * 10:
            return False

        return True
