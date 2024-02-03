
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.cars = []
        self.hideturtle()
        self.starting_position = 0
        self.pos = self.xcor()

    def create_car(self):
        for car_index in range(1):
            self.starting_position = random.randint(-230, 200)
            car_index = Turtle()
            car_index.penup()
            car_index.shape("square")
            car_index.setheading(180)
            car_index.shapesize(1, 2)
            car_index.color(random.choice(COLORS))
            self.cars.append(car_index)
            car_index.goto(280, self.starting_position)

    def move(self,level):
        if level == 1:
            return STARTING_MOVE_DISTANCE

        else:
            return STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1))





