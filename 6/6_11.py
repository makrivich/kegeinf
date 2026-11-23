from turtle import *
screensize(5000,5000)
tracer(0)
m=30
for _ in range(2):
    pd()
    for _ in range(2):
        fd(8*m)
        rt(90)
        fd(8*m)
        rt(90)
    pu()
    fd(6*m)
    rt(90)
    fd(6*m)
    lt(90)
rt(180)
fd(4*m)
pd()
for _ in range(4):
    fd(8*m)
    rt(270)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(5)
done()
