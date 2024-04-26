import streamlit as st
import random
import turtle

def modify_sierpinski(t, depth, length):
    if depth == 1:
        for _ in range(3):
            t.fd(length)
            t.lt(120)
    else:
        modify_sierpinski(t, depth - 1, length / 2)
        t.fd(length / 2)
        modify_sierpinski(t, depth - 1, length / 2)
        t.bk(length / 2)
        t.lt(60)
        t.fd(length / 2)
        t.rt(60)
        modify_sierpinski(t, depth - 1, length / 2)
        t.rt(120)
        t.fd(length / 2)
        t.lt(120)

def draw_sierpinski(depth, length):
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.tracer(0, 0)  # Disable automatic screen updates
    t.speed(0)  # Set maximum turtle speed
    t.penup()
    t.goto(-length / 2, -length / 2)  # Center the triangle
    t.pendown()
    modify_sierpinski(t, depth, length)
    screen.update()  # Update the screen once drawing is complete
    screen.mainloop()  # Keep the window open until manually closed

def main():
    st.title('Sierpinski Triangle')
    st.sidebar.header('Parameters')
    depth = st.sidebar.slider('Depth', min_value=1, max_value=7, value=3)
    length = st.sidebar.slider('Length', min_value=50, max_value=500, value=300)
    st.write('Adjust the parameters in the sidebar to change the Sierpinski triangle.')

    # Draw Sierpinski triangle
    draw_sierpinski(depth, length)

if __name__ == '__main__':
    main()

