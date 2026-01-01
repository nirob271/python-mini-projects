from turtle import *
import colorsys


speed(0)
bgcolor('black')
h = 0

for i in range(400):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005
    
    forward(i * 0.5)
    left(98)  
    
    forward(i * 0.2)
    left(59)
    forward(i * 0.1)

hideturtle()
done()