from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class ScoreBroad(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score_from_file()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_score_to_file()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over. >-<", align=ALIGNMENT, font=FONT)

    def save_score_to_file(self):
        with open("save_point.txt", mode="w") as file:
            file.write(str(self.high_score))

    def get_high_score_from_file(self):
        with open("save_point.txt", mode="r") as file:
            self.high_score = int(file.read().strip())
