import turtle
from turtle import *

t= Turtle()





#base
t.begin_fill()
t.fillcolor("red")

t.pu()
t.goto(0,0)
t.pd()
t.fd(5)
t.left(95)
t.fd(20)
t.rt(105)

#pétala direita
t.fd(20)
t.lt(105)
t.fd(10)
t.rt(75)
t.fd(30)
t.left(120)
t.fd(10)
t.rt(75)
t.fd(12)
t.lt(120)
t.fd(12)
t.rt(75)
t.fd(10)
t.lt(105)
t.fd(20)
t.rt(135)

#pétala superior
t.fd(22)
t.lt(135)
t.fd(12)
t.rt(105)
t.fd(29)

#até aqui tudo certo com o lado direito


#lado esquerdo agora
t.pu()
t.goto(0,0)
t.pd()
t.lt(70)
t.fd(5)


#base
t.pu()
t.goto(0,0)
t.pd()
t.fd(5)
t.rt(95)
t.fd(20)
t.lt(105)

#pétala direita
t.fd(20)
t.rt(105)
t.fd(10)
t.lt(75)
t.fd(30)
t.rt(120)
t.fd(10)
t.lt(75)
t.fd(12)
t.rt(120)
t.fd(12)
t.lt(75)
t.fd(10)
t.rt(105)
t.fd(20)
t.lt(135)

#pétala superior
t.fd(22)
t.rt(135)
t.fd(12)
t.lt(105)
t.fd(29)

t.end_fill()

t.pu()
t.lt(110)
t.rt(180)
t.goto(-150,-50)
t.pd()
for _ in range (2):
    t.forward(300)
    t.left(90)
    t.fd(200)
    t.lt(90)

t.begin_fill()
t.fillcolor("red")
for _ in range (2):
    t.fd(75)
    t.lt(90)
    t.fd(200)
    t.lt(90)
t.end_fill()

t.fd(225)
t.begin_fill()
t.fillcolor("red")
for _ in range (2):
    t.fd(75)
    t.lt(90)
    t.fd(200)
    t.lt(90)
t.end_fill()

mainloop()

