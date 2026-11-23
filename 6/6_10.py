from turtle import *
screensize(5000,5000)
tracer(0)
m=30
for _ in range(4):
    fd(12*m)
    lt(90)
pu()
rt(270)
bk(-7*m)
lt(180)
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
