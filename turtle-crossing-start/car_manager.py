from turtle import Turtle
import random 
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars=[]
        self.speed = MOVE_INCREMENT
        
        

    def create(self):
        chance = random.randint(1,6)
        if chance == 1:
            new = Turtle()
            new.shape("square")
            new.penup()
            new.shapesize(stretch_wid=1,stretch_len=2)
            new.color(random.choice(COLORS))
            random_y =random.randint(-150,150)
            new.goto(300,random_y)
            self.cars.append(new)



    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def levelup(self):
        self.speed += MOVE_INCREMENT





    
