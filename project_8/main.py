import turtle as t
import random as rd
import time as ti

t.bgcolor('yellow')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()


leaf = t.Turtle()

text_turtle = False
text_turtle = t.Turtle()
text_turtle.write('Press space to start', align='center', font=('Arial', 18,
                                                                'bold'))


score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)


ti.sleep(3)