# Allen, Sungmin, Yejun, Taiga
import turtle as trtl

t = trtl.Turtle()

t.speed(0)


# The Slope and Y-intecept
print("This program Creates a linear line (only positive) Y = mx + b")
m = int(input("Enter a number for m : "))
b = int(input("Enter a  number for b: "))


# coordanite plane


  # y hashmark
t.pencolor("grey")
x = 0
y_pos = -400
while x < 85:
    t.penup()
    t.goto(-400,y_pos)
    t.pendown()
    t.forward(800)
    t.backward(800)
    y_pos += 10
    x += 1 

  # y hashmark
t.setheading(0)
t.left(90)
y = 0
x_pos = -400
while y < 81:
    t.penup()
    t.goto(x_pos,-400 )
    t.pendown()
    t.forward(800)
    t.backward(800)
    x_pos += 10
    y += 1
       
  # Y & X axis
t.color("black")
t.pensize(3)
t.penup() 
t.goto(0,0) 
t.setheading(0) 
t.pendown() 
t.forward(400)
t.backward(800) 
t.goto(0,0) 
t.setheading(90) 
t.pendown 
t.forward(400) 
t.backward(800)

# The line

t.penup()
t.goto(0,0)

x_cor = 0
y_cor = 0

# b
t.color("red")
t.setheading(0)
t.penup()
t.forward(b)

# m

  #Line going up
for i in range(40):
  t.pendown()
  x_cor = m*i
  y_cor = x_cor + b
  t.goto(x_cor, y_cor)
  t.penup()
t.pendown()
t.left(45)
t.shape("arrow")
t.stamp()
t.penup()
t.goto(0,b)


  #Line going down
for i in range(40):
  t.pendown()
  x_cor = m*i
  y_cor = x_cor + b
  t.goto(-(x_cor), -(y_cor))
  t.penup()

t.pendown()
t.setheading(270)
t.right(45)
t.stamp()


wn = trtl.Screen()
wn.mainloop()