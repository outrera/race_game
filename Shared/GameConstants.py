import os


class GameConstants:

    SCREEN_SIZE = (800, 600)
    FPS = 60

    CAR_SIZE = [70, 120]  # Length/Width ~ 2.5
    CAR_SPEED = [5, 5]
    CAR_SPEED_NPC = [3, 3]

    LANE0_X = SCREEN_SIZE[0] / 8 * 2 + CAR_SIZE[0]/4
    LANE1_X = SCREEN_SIZE[0] / 8 * 3 + CAR_SIZE[0]/4
    LANE2_X = SCREEN_SIZE[0] / 8 * 4 + CAR_SIZE[0]/4
    LANE3_X = SCREEN_SIZE[0] / 8 * 5 + CAR_SIZE[0]/4

    SPRITE_CAR = os.path.join("Assets", "Graphics", "car_taxi2.png")
    SPRITE_CAR_BLACK1 = os.path.join("Assets", "Graphics", "car_black1.png")
    SPRITE_CAR_POLICE1 = os.path.join("Assets", "Graphics", "car_police1.png")
    SPRITE_CAR_POLICE2 = os.path.join("Assets", "Graphics", "car_police2.png")
    SPRITE_CAR_POLICE3 = os.path.join("Assets", "Graphics", "car_police3.png")
    SPRITE_CAR_TAXI1 = os.path.join("Assets", "Graphics", "car_taxi1.png")
    SPRITE_CAR_WHITE1 = os.path.join("Assets", "Graphics", "car_white1.png")
    SPRITE_CAR_WHITE2 = os.path.join("Assets", "Graphics", "car_white2.png")
    SPRITE_CAR_WHITE3 = os.path.join("Assets", "Graphics", "car_white3.png")
    SPRITE_CAR_WHITE4 = os.path.join("Assets", "Graphics", "car_white4.png")
    SPRITE_TRUCK_RED1 = os.path.join("Assets", "Graphics", "truck_red1.png")

    SPRITE_BACKGROUND = os.path.join("Assets", "Graphics", "four_lanes_road.png")
    SPRITE_CAR_CRASH = os.path.join("Assets", "Graphics", "car_crash.png")
    SPRITE_HIGH_SCORE = os.path.join("Assets", "Graphics", "trophy.png")

    PLAYING_SCENE = 0
    GAMEOVER_SCENE = 1
    HIGHSCORE_SCENE = 2
    MENU_SCENE = 3