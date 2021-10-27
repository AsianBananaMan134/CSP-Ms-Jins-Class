#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0

# iterate
while floor < num_floors:
  if (floor % 21 == 0):
    x = x + 100
    y = -150

  painter.penup()
  painter.goto(x,y)

  painter.color("gray")
  rem = floor % 9

  if (rem > 2):
    painter.color("blue")

  if (rem > 5):
    painter.color("red")

  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  y = y + 5 # location of next floor
  floor = floor + 1
   
  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()