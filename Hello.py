import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

def modify_sierpinski(ax, t, depth, length):
    if depth == 1:
        t.set_data([t.get_xdata(), [t.get_ydata()[0], t.get_ydata()[0] + length]])
    else:
        modify_sierpinski(ax, t, depth - 1, length / 2)
        ax.draw_artist(t)
        ax.figure.canvas.draw()
        t.set_ydata([t.get_ydata()[0], t.get_ydata()[0] + length])
        t.set_xdata([t.get_xdata()[0] + length / 2, t.get_xdata()[1]])
        ax.draw_artist(t)
        ax.figure.canvas.draw()
        modify_sierpinski(ax, t, depth - 1, length / 2)
        ax.draw_artist(t)
        ax.figure.canvas.draw()
        t.set_ydata([t.get_ydata()[0], t.get_ydata()[0]])
        t.set_xdata([t.get_xdata()[0] - length / 4, t.get_xdata()[1] - length / 2])
        ax.draw_artist(t)
        ax.figure.canvas.draw()
        modify_sierpinski(ax, t, depth - 1, length / 2)
        ax.draw_artist(t)
        ax.figure.canvas.draw()

def animate(i):
    modify_sierpinski(ax, line, i, 300)
    return line,

def main():
    fig, ax = plt.subplots()
    ax.set_xlim([-150, 150])
    ax.set_ylim([0, 260])
    line, = ax.plot([0, 0], [0, 0])
    ani = FuncAnimation(fig, animate, frames=7, interval=1000, blit=True)
    st.write(ani.to_jshtml())

if __name__ == '__main__':
    main()
