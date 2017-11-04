import time
import turtle

t = turtle.Pen()
x = -250
y = 200
t.penup()
t.goto(x, y)
t.pendown()
for j in range(0, 10):
    x += 120
    if j == 4:
        x = -250
        y -= 120
    for i in range(0, 5):
        t.forward(100)
        t.right(144)
        time.sleep(0.1)
    t.penup()
    t.goto(x, y)
    t.pendown()
t.reset()
