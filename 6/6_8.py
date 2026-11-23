from turtle import *
screensize(5000,5000)
tracer(0)
m=30
for _ in range(4):
    fd(3*m)
    lt(270)
    fd(5*m)
    rt(90)
lt(270)
for _ in range(3):
    fd(5*m)
    rt(90)
    fd(3*m)
    lt(270)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(5)
done()
