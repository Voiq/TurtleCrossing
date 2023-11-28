import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_is_on = True

#Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


#Player
player=Player()
#Car Manager
car_manager=CarManager()
#Scoreboard
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(player.go_up,"w")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move()
    
    # detect collision
    for  cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on=False
            scoreboard.game_over()
            
            
    #Detect if turtle has finished
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
                
screen.exitonclick()
