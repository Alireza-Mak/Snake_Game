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
        with open("./data.txt", "r") as data_file:
            self.high_score = int(data_file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT1)
        self.goto(0, -270)
        self.write('To quit the game press "q"', align=ALIGNMENT, font=FONT3)

    def quit(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Created by Alireza Mak.", align=ALIGNMENT, font=FONT2)
        self.goto(0, -50)
        self.write("Alirezamak.com", align=ALIGNMENT, font=FONT3)

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", "w") as data_file:
                data_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
