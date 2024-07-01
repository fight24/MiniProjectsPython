from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBroad(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_text_level()

    def create_text_level(self):
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_increase(self):
        self.level += 1
        self.clear()
        self.create_text_level()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=FONT)