import turtle   
turtle.speed(0)          
colors = [ "red","purple","blue","green","orange","yellow"]
t1 = turtle.Pen()
turtle.bgcolor("black")
for x in range(72):
   t1.pencolor(colors[x % 6])
   t1.width(x/100)
   t1.forward(x)
   t1.left(59)
turtle.done()   