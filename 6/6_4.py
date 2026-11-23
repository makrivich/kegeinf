from turtle import *
screensize(5000,5000)
tracer(0)
m=30
for _ in range(9):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)
pu()
fd(1*m)
rt(90)
fd(5*m)
lt(90)
pd()
for _ in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(5)
done()