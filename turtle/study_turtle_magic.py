import turtle as tl


def buildcircle(r, step=0):
    t.penup()
    t.sety(-r)
    t.pendown()
    if (step == 0):
        t.circle(r)
    else:
        t.circle(r, steps=step)


def build_min_circle(r, x, y):
    t.penup()
    t.goto(x, y - r)
    t.right(60)
    t.pendown()
    t.circle(r)
    t.penup()
    t.goto(x, y)
    t.left(60)
    t.pendown()


def fbuild(time, le, jiaodu, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(0, time):
        t.left(jiaodu)
        t.forward(le)
        # build_min_circle(10, t.xcor(), t.ycor())


t = tl.Pen()
t.speed(0.3)
t.color('red', 'yellow')
x = 0
y = 0
# t.begin_fill()
buildcircle(300)
buildcircle(200)
buildcircle(-200, 6)
buildcircle(100)
buildcircle(-50, 6)
buildcircle(20)
# t.end_fill()
t.left(90)
for i in range(0, 6):
    t.penup()
    t.goto(0, 0)
    t.left(60)
    t.forward(100)

    t.right(90)
    t.pendown()
    t.circle(50, steps=6)
    t.left(90)

    t.circle(25)
    t.left(180)
    t.circle(25)
    t.right(180)

    t.penup()
    t.forward(100)

    t.penup()
    t.forward(100)
    t.left(90)
    t.pendown()
    t.circle(100)
    t.right(90)
    t.left(90)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.right(90)

# fbuild(6,50,60,25,-43.3)
# fbuild(6,200,60,100,-173.2)
# t.hideturtle()
tl.done()
