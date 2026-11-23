from turtle import *
screensize(5000,5000)
tracer(0)
m=30
rt(30)
for _ in range(3):
    rt(150)
    fd(6*m)
    rt(30)
    fd(12*m)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(5)
done()