from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-280, 250)
GAME_OVER_POSITION = (0, 0)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self) -> None:
        self.level += 1
        self.update_scoreboard()

    def game_over(self) -> None:
        self.goto(GAME_OVER_POSITION)
        self.write("GAME OVER", align="center", font=FONT)
