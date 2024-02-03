import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car = CarManager()
screen.listen()
screen.onkeypress(player.up, "Up")
level = 1


game_is_on = True


counter = 0
val_counter = 15

while game_is_on:
    counter_increment = 1 * level

    if counter % val_counter == 0:
        car.create_car()
    for vehicle in car.cars:
        new_vehicle_x = vehicle.xcor()
        new_vehicle_y = vehicle.ycor()
        player_cor_x = player.xcor()
        player_cor_y = player.ycor()
        collision = player.distance(vehicle)
        vehicle.forward(car.move(level))
        if player.distance(vehicle) < 25 and player.ycor() - vehicle.ycor() < 15:
            player.go_home()

    time.sleep(0.1)
    screen.update()
    if player.ycor() > 280:
        player.go_home()
        scoreboard.level_up()
        level += 1
        if val_counter > 5:
            val_counter -= 5
        elif val_counter > 1:
            val_counter -= 1
        elif val_counter > 0.1:
            val_counter -= 0.1
        print(counter_increment)

    counter += 1

    # print(counter, counter_increment)


screen.exitonclick()
