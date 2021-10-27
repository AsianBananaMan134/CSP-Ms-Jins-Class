#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# loop to pop "gold" and use colors to fill and to draw in order
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)

  new_color = turtle_colors.pop()

  t.fillcolor(new_color)
  t.pencolor(new_color)

  my_turtles.append(t)
  t.penup()

# the initials
startx = 0
starty = 0

direction = t.heading()
direction = 45

# loop the initialized turtles
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(direction)    
  t.pendown()
  t.forward(50)

#	modify the x and y 
  startx = t.xcor()
  starty = t.ycor()

  direction -= 45

wn = trtl.Screen()
wn.mainloop()