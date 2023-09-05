from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.color("white")
        self.current_score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write(f"Score = {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
