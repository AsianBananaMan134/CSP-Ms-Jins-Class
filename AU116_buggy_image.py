#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

spider.pensize(40)
spider.circle(20)

"""
hi
"""

spider_legs = 8
leg_length = 70
leg_angle = 380 / spider_legs
spider.pensize(5)

counter = 0
while (counter < spider_legs):
  spider.goto(0,0)
  spider.setheading(leg_angle*counter)
  spider.forward(leg_length)
  counter = counter + 1

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()