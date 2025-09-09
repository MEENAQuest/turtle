import turtle             
t1 = turtle.Turtle()

t1.width(5)  
t1.color('red')
t1.write("Python Turtle!", font=("Arial", 20, "normal"))
t1.penup()
t1.goto(50, -50)
t1.color('green')
t1.pendown()  

for i in range(4):
   t1.forward(50)           
   t1.right(90)       
turtle.done()