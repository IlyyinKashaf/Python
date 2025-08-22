from turtle import Turtle

STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 240
FONT = ("Arial",14,"normal")
ALIGNMENT="center"


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.origin()
        self.setheading(90)



    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def game_over(self):
        self.write(f"Game Over",align= ALIGNMENT , font= FONT)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False 
    def origin(self):
        self.goto(STARTING_POSITION)

  
