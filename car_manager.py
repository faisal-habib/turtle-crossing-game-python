from random import choice, randint
from turtle import Turtle

from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# A car is a square stretched from Turtle's default 20 x 20 px size,
# so these values make it 20 px tall and 40 px long.
CAR_STRETCH_WIDTH = 1
CAR_STRETCH_LENGTH = 2

CAR_START_X = 300
CAR_MIN_Y = -250
CAR_MAX_Y = 250
CAR_APPEAR_INTERVAL = 6  # a new car appears on average once every 6 frames
COLLISION_DISTANCE = 20

# Half the screen width (300) plus half a car's length (20):
# a car this far left is completely off-screen.
OFF_SCREEN_X = -320

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self) -> None:
        if randint(1, CAR_APPEAR_INTERVAL) == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=CAR_STRETCH_WIDTH, stretch_len=CAR_STRETCH_LENGTH)
            car.penup()
            car.color(choice(COLORS))
            random_y = randint(CAR_MIN_Y, CAR_MAX_Y)
            car.goto(CAR_START_X, random_y)
            self.all_cars.append(car)

    def move_cars(self) -> None:
        for car in self.all_cars:
            car.backward(self.car_speed)

        self._remove_off_screen_cars()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def is_colliding_with(self, player: Player):
        for car in self.all_cars:
            if car.distance(player) < COLLISION_DISTANCE:
                return True

        return False

    def _remove_off_screen_cars(self) -> None:
        still_on_screen = []

        for car in self.all_cars:
            if car.xcor() > OFF_SCREEN_X:
                still_on_screen.append(car)
            else:
                car.hideturtle()
        self.all_cars = still_on_screen
