from turtle import *
import math

# Name your Turtle.
tutu = Turtle()

# Set Up your screen and starting position.
setup(50,50)
x_pos = 50
y_pos = 50

### Write your code below:
###tutu.forward(150)
# tutu.right(90)
# tutu.forward(150)
# tutu.left(90)
# tutu.backward(150)
# tutu.right(90)
# tutu.backward(150)

number = int(input ("Please write how many sides the polygon has"))
color = input ("Choose a filling color")
tutu.color("color")
tutu.begin_fill()
def shape():
    while number < number + 1:
        tutu.forward(100)
        tutu.left(360/number)
tutu.end_fill()

shape()



# Close window on click.
exitonclick()

