from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.pencolor("white")
        self.current_score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.current_score += 1
        self.write(f"Score = {self.current_score}", align="center", font=('Arial', 14, 'normal'))


