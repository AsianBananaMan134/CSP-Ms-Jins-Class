# a121_catch_a_turtle.py
# -----import statements-----
import turtle as trtl
import random as rand

spot = trtl.Turtle()
score_writer = trtl.Turtle()
t = trtl.Turtle()

# -----make the graphing cords----
t.speed(0)
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
   
# -----game configuration----
spot_shape = "triangle"
spot_color = "blue"
spot_fill_color = "blue"
score = 0 

score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-450,300)
score_writer.pendown()

font_setup = ("Arial", "20", "normal")

# -----initialize turtle-----
spot.shape(spot_shape)
spot.color(spot_color)
spot.fillcolor(spot_fill_color)

# -----game functions--------
def spot_clicked(x, y):
  change_position()
  print("HEY STOP CALLING ME A MONKEY!")
  updated_score()

def updated_score():
  score_writer.clear()
  global score
  score += 1
  score_writer.write(score, font = font_setup)

def change_position():
  spot.penup()
  new_xpos = rand.randint(-300,300)
  new_ypos = rand.randint(-400,400)
  spot.goto(new_xpos, new_ypos)

# -----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.mainloop()