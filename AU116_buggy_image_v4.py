#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

# draw spider body
spider.pensize(40)
spider.circle(20)

"""
hi
"""

# configure spider legs
spider_legs = 4
leg_length = 70
leg_angle = 90 / spider_legs
spider.pensize(5)

# draw the legs
incrementing_counter = 0
while (incrementing_counter < spider_legs):
  spider.goto(0,20)
  spider.setheading(leg_angle * incrementing_counter - 45)
  spider.forward(leg_length)
  incrementing_counter = incrementing_counter + 1
spider.hideturtle()

spider_legs = 4
incrementing_counter = 4
leg_angle = -90 / spider_legs
while(incrementing_counter < spider_legs + 4):
  spider.goto(0,20)
  spider.setheading(leg_angle * incrementing_counter - 45)
  spider.forward(leg_length)
  incrementing_counter = incrementing_counter + 1
spider.hideturtle()

# draw eyes
spider.penup()
spider.goto(10,30)
spider.color("red")
spider.pensize(5)
spider.begin_fill()
spider.pendown()
spider.circle(1)
spider.penup()
spider.end_fill()
spider.goto(-10,30)
spider.pendown()
spider.circle(1)


wn = trtl.Screen()
wn.mainloop()