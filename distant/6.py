from turtle import *
tracer(0)
lt(90)
m=30
for _ in range(2):
    fd(5*m);lt(270);bk(8*m);lt(270)
pu()
fd(2*m);rt(90);bk(3*m);lt(90)
pd()
for _ in range(3):
    fd(8*m);lt(270);fd(4*m);lt(270)
pu()
fd(4*m);rt(90);bk(2*m)
pd()
for _ in range(3):
    fd(5*m);rt(90);fd(7*m);rt(90)
pu()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3)
done()
