from turtle import *
screensize(5000,5000)
tracer(0)
m=30
for _ in range(4):
    fd(10*m)
    rt(270)
pu()
fd(3*m)
rt(270)
fd(5*m)
rt(90)
pd()
for _ in range(2):
    fd(10*m)
    rt(270)
    fd(12*m)
    rt(270)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(5)
done()
