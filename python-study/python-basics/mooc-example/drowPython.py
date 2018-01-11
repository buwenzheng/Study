# !/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle

def drowSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 800, 100, 100)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor('#0f0')
    turtle.seth(0)
    drowSnake(5, 80, 5, pythonsize*2)

main()