from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",14,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.color("white")
        self.penup()
        self.goto(0,170)
        self.hideturtle()
        self.update()


    def update(self):
         
         self.write(f"Score : {self.score}",align= ALIGNMENT , font= FONT)


    def scoreupdate(self):
        
        self.score +=1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT , font= FONT)


