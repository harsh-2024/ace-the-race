from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

def forward_move():
    timmy.forward(10)

def backward_move():
    timmy.backward(10)

def turn_left():
    timmy.setheading(timmy.heading()+90)

def turn_right():
    timmy.setheading(timmy.heading()-90)

def return_back():
    timmy.penup()
    timmy.home()

def clear_draw():
    timmy.clear()


my_screen.listen()

my_screen.onkey(key="w", fun=forward_move)
my_screen.onkey(key="s", fun=backward_move)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="b", fun=return_back)
my_screen.onkey(key="c", fun=clear_draw)

my_screen.exitonclick()





