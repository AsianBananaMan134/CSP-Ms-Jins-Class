#   a116_ladybug.py
import turtle as trtl

# create the ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

leg_nums = 6
ladybug.pensize(5)
for i in range(leg_nums):
  ladybug.penup()
  ladybug.goto(0,-35)
  ladybug.pendown()
  heading = (260/leg_nums) * i - (260/leg_nums)
  if i > 2:
    heading += 50
  ladybug.setheading(heading)
  ladybug.forward(50)

ladybug.setheading(0)

# make the body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# make the dots
num_dots = 1
x_position = -20
y_position = -55
ladybug.pensize(10)

# draw the dots
while num_dots <= 2:
  ladybug.penup()
  ladybug.goto(x_position, y_position)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(x_position + 30, y_position + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position the next dots
  x_position = x_position + 5
  y_position = y_position + 25
  num_dots += 1

ladybug.hideturtle()
wn = trtl.Screen()
wn.mainloop()