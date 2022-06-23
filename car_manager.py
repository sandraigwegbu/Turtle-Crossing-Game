from turtle import Turtle
import random

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5  # how much the move distance should increase every time the user levels up


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed_variable = 0

    def create_car(self):
        random_chance = random.randint(1, 6)  # to generate a new car only every 6th time in the game loop
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.turtlesize(stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            new_car.goto(x=310, y=random.randint(-230, 230))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE + self.speed_variable)

    def increase_speed(self):
        self.speed_variable += MOVE_INCREMENT
