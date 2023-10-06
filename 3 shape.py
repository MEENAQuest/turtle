import turtle             
t1 = turtle.Turtle()
side = int(input("Enter number of sides: "))
my_angle = 360.0 / side
for i in range(side):
   t1.forward(70)           
   t1.right(my_angle) 
turtle.done()