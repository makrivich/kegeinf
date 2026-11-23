from turtle import *
screensize(5000,5000)
tracer(0)
m=30
for _ in range(2):
    fd(24*m)
    rt(90)
    fd(16*m)
    rt(90)
pu()
fd(10*m)
rt(90)
fd(8*m)
lt(90)
pd()
for _ in range(2):
    fd(15*m)
    rt(90)
    fd(28*m)
    rt(90)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(5)
done()