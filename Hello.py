import streamlit as st
import turtle
import random
import tkinter

def modify_sierpinski(t, depth, length):
    t.pd()
    t.pensize(random.randrange(0, 10))
    if depth == 1:
        t.lt(60)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(180)
    else:
        modify_sierpinski(t, depth - 1, length / 2)
        t.fd(length / 2)
        t.color(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
        modify_sierpinski(t, depth - 1, length / 2)
        t.color(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
        t.bk(length / 2)
        t.lt(60)
        t.fd(length / 2)
        t.rt(60)
        modify_sierpinski(t, depth - 1, length / 2)
        t.color(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
        t.rt(120)
        t.fd(length / 2)
        t.lt(120)

# Streamlit code
st.title("Sierpinski Triangle")



t = turtle.RawTurtle(screen)
t.speed(10)
modify_sierpinski(t, 4, 200)
screen.bye()
