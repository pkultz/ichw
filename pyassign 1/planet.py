import math
pi = math.pi

import turtle
t0,t1,t2,t3,t4,t5,t6 = range(7)
planet = [t0,t1,t2,t3,t4,t5,t6]
color = ["yellow","blue","green","red","black","orange","skyblue"]
a = range(0,301,50)
b = range(0,241,40)

for i in range(7):
    planet[i] = turtle.Turtle()
    planet[i].color(color[i])
    planet[i].shape("circle")
    planet[i].speed(0)

for i in range(1,7):
    planet[i].up()
    c = math.sqrt(abs(a[i] ** 2 - b[i] ** 2))
    planet[i].forward(a[i] + c)
    planet[i].down()

x = 150
k = 100
for n in range(k * x):
        for i in range(1,7):
            m1 = n * 2 * pi / (i * x)
            m2 = (n + 1) * 2 * pi / (i * x)
            x1 = a[i] * math.cos(m1)
            x2 = a[i] * math.cos(m2)
            y1 = b[i] * math.sin(m1)
            y2 = b[i] * math.sin(m2)
            dx = x2 - x1
            dy = y2 - y1
            planet[i].forward(dx)
            planet[i].left(90)
            planet[i].forward(dy)
            planet[i].left(-90)
