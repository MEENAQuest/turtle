import turtle  
t1 = turtle.Turtle()  
turtle.speed(0)  

t1.penup()  
t1.goto(-200, 125)  
t1.pendown()  
 
t1.color("orange")  
t1.begin_fill()  
t1.forward(400)  
t1.right(90)  
t1.forward(84)  
t1.right(90)  
t1.forward(400)  
t1.end_fill()  

t1.color("white") 
t1.left(90)  
t1.forward(84)  
    
t1.color("green")  
t1.begin_fill()  
t1.left(90) 
t1.forward(400)  
t1.right(90)  
t1.forward(84)  
t1.right(90)  
t1.forward(400)  
t1.end_fill()  
  
t1.penup()  
t1.goto(0,35)  
t1.pendown() 
t1.pensize(2) 
t1.color("navy")   
t1.circle(35)    
  
t1.color("navy")  
t1.penup()  
t1.goto(0, 10)  
t1.pendown()  
t1.begin_fill()  
t1.circle(10)  
t1.end_fill()  
   
t1.penup()  
t1.goto(0, 0)  
t1.pendown()  
t1.pensize(2)  
for j in range(24):  
    t1.forward(32)  
    t1.backward(32)  
    t1.left(15)  
    
t1.hideturtle()    
turtle.done()  