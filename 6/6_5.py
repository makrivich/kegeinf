from turtle import *
screensize(5000, 5000)
tracer(0)
m = 10
for _ in range(4):
    fd(19 * m)
    rt(90)
    fd(30 * m)
    rt(90)
pu()
fd(2 * m)
rt(90)
fd(8 * m)
lt(90)
pd()
for _ in range(4):
    fd(93 * m)
    rt(90)
    fd(97 * m)
    rt(90)
pu()
for x in range(-10, 120):
    for y in range(-10, 120):
        goto(x * m, y * m)
        dot(4)
done()
