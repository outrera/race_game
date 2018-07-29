import os


class GameConstants:

    def __init__(self):
        # load all graphic resources once

        pass

    SCREEN_SIZE = (800, 600)
    FPS = 60

    CAR_SIZE = [70, 120]  # Length/Width ~ 2.5
    CAR_SPEED = [5, 5]
    CAR_SPEED_NPC = [3, 3]

    TRUCK_LONG_SIZE = [80, 240]
    TRUCK_MEDIUM_SIZE = [80, 180]
    BUS_SIZE = [80, 220]

    BUSH_SIZE = [30, 30]
    HOUSE_SIZE = [[120, 120], [120, 100], [150, 100], [100, 150]]
    TREE_SIZE = [70, 70]

    LANE0_X = SCREEN_SIZE[0] / 8 * 2 + CAR_SIZE[0] / 4
    LANE1_X = SCREEN_SIZE[0] / 8 * 3 + CAR_SIZE[0] / 4
    LANE2_X = SCREEN_SIZE[0] / 8 * 4 + CAR_SIZE[0] / 4
    LANE3_X = SCREEN_SIZE[0] / 8 * 5 + CAR_SIZE[0] / 4
    LANE_SIZE = SCREEN_SIZE[0] / 8

    VEHICLES = {
        "SPRITE_CAR_BLACK1": os.path.join("Assets", "Graphics", "car_black1.png"),
        "SPRITE_CAR_BLUE1": os.path.join("Assets", "Graphics", "car_blue1.png"),
        "SPRITE_CAR_BLUE2": os.path.join("Assets", "Graphics", "car_blue2.png"),
        "SPRITE_CAR_BROWN1": os.path.join("Assets", "Graphics", "car_brown1.png"),
        "SPRITE_CAR_BROWN2": os.path.join("Assets", "Graphics", "car_brown2.png"),
        "SPRITE_CAR_TAXI1": os.path.join("Assets", "Graphics", "car_taxi1.png"),
        "SPRITE_CAR_TAXI2": os.path.join("Assets", "Graphics", "car_taxi2.png"),
        "SPRITE_CAR_WHITE1": os.path.join("Assets", "Graphics", "car_white1.png"),
        "SPRITE_CAR_WHITE2": os.path.join("Assets", "Graphics", "car_white2.png"),
        "SPRITE_CAR_WHITE3": os.path.join("Assets", "Graphics", "car_white3.png"),
        "SPRITE_CAR_WHITE4": os.path.join("Assets", "Graphics", "car_white4.png"),
        "SPRITE_CAR_GREEN1": os.path.join("Assets", "Graphics", "car_green1.png"),
        "SPRITE_CAR_GREEN2": os.path.join("Assets", "Graphics", "car_green2.png"),

        "SPRITE_CAR_POLICE1": os.path.join("Assets", "Graphics", "car_police1.png"),
        "SPRITE_CAR_POLICE2": os.path.join("Assets", "Graphics", "car_police2.png"),
        "SPRITE_CAR_POLICE3": os.path.join("Assets", "Graphics", "car_police3.png"),

        "SPRITE_BUS_YELLOW1": os.path.join("Assets", "Graphics", "bus_yellow1.png"),
        "SPRITE_TRUCK_LONG1": os.path.join("Assets", "Graphics", "truck_long1.png"),
        "SPRITE_TRUCK_LONG2": os.path.join("Assets", "Graphics", "truck_long2.png"),
        "SPRITE_TRUCK_MEDIUM1": os.path.join("Assets", "Graphics", "truck_medium1.png"),
        "SPRITE_TRUCK_MEDIUM2": os.path.join("Assets", "Graphics", "truck_medium2.png")
    }

    OFF_ROAD_OBSTACLES = {
        "SPRITE_BUSH1": os.path.join("Assets", "Graphics", "bush1.png"),
        "SPRITE_BUSH2": os.path.join("Assets", "Graphics", "bush2.png"),
        "SPRITE_BUSH3": os.path.join("Assets", "Graphics", "bush3.png"),
        "SPRITE_BUSH4": os.path.join("Assets", "Graphics", "bush4.png"),
        "SPRITE_BUSH5": os.path.join("Assets", "Graphics", "bush5.png"),
        "SPRITE_BUSH6": os.path.join("Assets", "Graphics", "bush6.png"),
        "SPRITE_HOUSE1": os.path.join("Assets", "Graphics", "house1.png"),
        "SPRITE_HOUSE2": os.path.join("Assets", "Graphics", "house2.png"),
        "SPRITE_HOUSE3": os.path.join("Assets", "Graphics", "house3.png"),
        "SPRITE_HOUSE4": os.path.join("Assets", "Graphics", "house4.png"),
        "SPRITE_HOUSE5": os.path.join("Assets", "Graphics", "house5.png"),
        "SPRITE_HOUSE6": os.path.join("Assets", "Graphics", "house6.png"),
        "SPRITE_HOUSE7": os.path.join("Assets", "Graphics", "house7.png"),
        "SPRITE_TREE1": os.path.join("Assets", "Graphics", "tree1.png"),
        "SPRITE_TREE2": os.path.join("Assets", "Graphics", "tree2.png"),
        "SPRITE_TREE3": os.path.join("Assets", "Graphics", "tree3.png"),
        "SPRITE_TREE4": os.path.join("Assets", "Graphics", "tree4.png"),
        "SPRITE_TREE5": os.path.join("Assets", "Graphics", "tree5.png"),
        "SPRITE_TREE6": os.path.join("Assets", "Graphics", "tree6.png"),
        "SPRITE_TREE7": os.path.join("Assets", "Graphics", "tree7.png")
    }

    SPRITE_MENU = os.path.join("Assets", "Graphics", "menu_background.png")
    SPRITE_BACKGROUND = os.path.join("Assets", "Graphics", "four_lanes_road.png")
    SPRITE_ROAD_MARKING = os.path.join("Assets", "Graphics", "road_surface_marking.png")
    SPRITE_CAR_CRASH = os.path.join("Assets", "Graphics", "car_crash.png")
    SPRITE_HIGH_SCORE = os.path.join("Assets", "Graphics", "trophy.png")

    PLAYING_SCENE = 0
    GAMEOVER_SCENE = 1
    HIGHSCORE_SCENE = 2
    MENU_SCENE = 3
