import turtle
# Set up the turtle screen and set the background color to white
screen = turtle.Screen()
screen.bgcolor("white")
# Create a new turtle and set its speed to the fastest possible
t1 = turtle.Turtle()
t1.speed(0)
# Set the fill color to red
t1.fillcolor("red")
t1.begin_fill()
# Draw the circle with a radius of 100 pixels
t1.circle(100)
# End the fill and stop drawing
t1.end_fill()
t1.hideturtle()
# Keep the turtle window ot1 until it is manually closed
turtle.done()