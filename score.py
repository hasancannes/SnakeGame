from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-250,270)
        self.hideturtle()
        self.uptade_scoreboard()
        
    def uptade_scoreboard(self):
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 15, "normal"))
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.uptade_scoreboard()