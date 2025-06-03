import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Maze Runner")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Draw walls (simple square maze)
walls = turtle.Turtle()
walls.color("yellow")
walls.pensize(4)
walls.hideturtle()
walls.speed(0)

walls.penup()
walls.goto(-250, 250)
walls.pendown()
for _ in range(4):
    walls.forward(500)
    walls.right(90)

walls.penup()
walls.goto(-100, 250)
walls.pendown()
walls.right(90)
walls.forward(300)

walls.penup()
walls.goto(100, -50)
walls.pendown()
walls.left(90)
walls.forward(300)

# Create Player Turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(-220, 220)
player.shapesize(stretch_wid=3, stretch_len=3)

# Movement Functions
def move_up():
    player.setheading(90)
    player.forward(20)

def move_down():
    player.setheading(270)
    player.forward(20)

def move_left():
    player.setheading(180)
    player.forward(20)

def move_right():
    player.setheading(0)
    player.forward(20)

# Key Bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

screen.mainloop()