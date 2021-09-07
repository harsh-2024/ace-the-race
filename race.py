from turtle import Turtle, Screen
import random

my_screen = Screen()
colors = ["red", "blue", "cyan", "purple", "magenta", "yellow"]

my_screen.setup(height=500, width=600)
user_bet = my_screen.textinput(title="User Bet", prompt=f" Which turtle is going to win? Choose any one color from {colors}: ")
my_screen.title("Turtle race")

all_turtles = []

is_race_on = False

if user_bet:
    is_race_on = True


for turtle_index in range(0,6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[turtle_index])
    timmy.goto(x=-290, y=0+(turtle_index*30))
    all_turtles.append(timmy)


while is_race_on:
    pace = random.randint(0,10)
    member = random.randint(0,5)
    all_turtles[member].forward(pace*5)
    if all_turtles[member].xcor() > 270:
        is_race_on = False
        if user_bet.lower() == colors[member]:
            print(f"You've won and the winner is {colors[member]}")
        else:
            print(f"You've lost and the winner is {colors[member]}")

my_screen.exitonclick()

