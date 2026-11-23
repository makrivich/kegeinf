from turtle import *
screensize(5000,5000)
tracer(0)
m=30
for _ in range(777):
    fd(25*m)
    lt(90)
    fd(34*m)
    lt(90)
pu()
fd(12*m)
lt(90)
fd(17*m)
rt(90)
pd()
for _ in range(1996):
    fd(25*m)
    lt(90)
    fd(17*m)
    lt(90)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(5)
done()
