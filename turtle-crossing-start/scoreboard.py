from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 200)  # Positioned at the top-left corner for better visibility
        self.update_score()

    def update_score(self):
        """Clears the previous score and displays the updated score."""
        self.clear()
        self.write(f"LEVEL: {self.score}", align="left", font=FONT)

    def inc_level(self):
        """Increments the score and updates the display."""
        self.score += 1
        self.update_score()




        

    
