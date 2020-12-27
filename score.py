from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        self.save()

    def save(self):
        open("high_score.txt", "w").close()
        file = open(r"high_score.txt", "w")
        file.write(str(self.high_score))
        file.close()

    def load_high_score(self):
        file = open(r"high_score.txt", "r")
        self.high_score = int(file.read())