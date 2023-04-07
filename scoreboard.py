from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.color("black")
        self.write_level()

    def write_level(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def show_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
