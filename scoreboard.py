from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 12, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()   # Otherwise, turtle will show along with the whatever you write at title.
        self.color("white")     # to change  the font of turtle from default black to white
        self.goto(0, 270)       # because by default turtle is at (0, 0)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)    # This function writes
        # where turtle is currently located, and therefore we changed the turtle's co-ordinates in __init__.

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.refresh_score()

