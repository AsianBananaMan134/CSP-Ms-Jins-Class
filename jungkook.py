import turtle as trtl

p = trtl.Turtle()
p.speed(0)

p.penup()
p.goto(100,0)


# Shirt circle
p.color("grey")
p.penup()
p.goto(100,0)
p.pendown()
p.circle(50)


# draw an oval
p.pendown()
p.left(45)
for loop in range(2):
    p.color("peachpuff")
    p.begin_fill()
    p.circle(150,90)
    p.circle(75,90)
    p.end_fill()
p.right(45)
p.color("grey")


# Big frame Line 
p.penup()
p.goto(-400,-50)
p.pendown()
p.forward(800)

p.penup()
p.goto(400,-50)

# right arm
p.penup()
p.goto(300,-50)
p.pendown()
p.left(135)
p.forward(150)
p.left(25)
p.forward(50)

# left arm
p.penup()
p.forward(210)
p.left(90)
p.forward(20)
p.right(90)
p.left(25)
p.pendown()
p.forward(200)
p.right(160)
p.forward(150)
p.left(90)
p.forward(50)
p.left(90)
p.forward(200)
p.left(67)
p.forward(200)
p.left(90)
p.forward(200)

# face
p.penup()
p.goto(0, 100)
p.setheading(-60)
p.width(5)
p.pendown()
p.circle(80, 120)  # draw smile

p.fillcolor("black")

for i in range(2):
    p.penup()
    p.goto(i, 35)
    p.setheading(50)
    p.pendown()
    p.begin_fill()
    p.circle(10)  # draw eyes
    p.end_fill()



wn = trtl.Screen()
wn.mainloop()
