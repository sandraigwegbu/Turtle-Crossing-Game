from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)  # tracer(0) turns off the animation
screen.listen()


player = Player()
screen.onkeypress(key="Up", fun=player.move)

car_manager = CarManager()
scoreboard = Scoreboard()

# Let's play
game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()  # updates the screen when tracer(0) is in use

    # Create the car behaviour
    car_manager.create_car()
    car_manager.move_cars()

    # Detect when the Turtle collides with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 30 and car.xcor() < 40:
            scoreboard.game_over()
            time.sleep(3)
            game_is_on = False

    # Detect when the Turtle has reached the other side
    if player.ycor() > FINISH_LINE_Y:
        player.return_position()
        car_manager.increase_speed()
        scoreboard.update_score()
