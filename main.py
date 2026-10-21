import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FRAME_DELAY_SECONDS = 0.1


def main() -> None:
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.go_up, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(FRAME_DELAY_SECONDS)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        # Detect collision with car
        if car_manager.is_colliding_with(player):
            game_is_on = False
            scoreboard.game_over()

        # Detect successful player crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()
    screen.exitonclick()

if __name__ == '__main__':
    main()