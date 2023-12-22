from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Courier", 24, "normal")
FONT2 = ("Courier", 20, "bold")
FONT3 = ("Courier", 16, "bold")


# TODO 6: Create Food class for snake and its methods
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT1)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT1)
        self.goto(0, -50)
        self.write("Created by Alireza Mak.", align=ALIGNMENT, font=FONT2)
        self.goto(0, -100)
        self.write("Alirezamak.com", align=ALIGNMENT, font=FONT3)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
