import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def draw_triangle(ax, p1, p2, p3):
    ax.plot([p1[0], p2[0], p3[0], p1[0]], [p1[1], p2[1], p3[1], p1[1]], 'k-')

def sierpinski(ax, p1, p2, p3, level):
    if level == 0:
        draw_triangle(ax, p1, p2, p3)
    else:
        p12 = (p1 + p2) / 2
        p23 = (p2 + p3) / 2
        p31 = (p3 + p1) / 2
        sierpinski(ax, p1, p12, p31, level - 1)
        sierpinski(ax, p12, p2, p23, level - 1)
        sierpinski(ax, p31, p23, p3, level - 1)

def main():
    st.title("Sierpinski Triangle")

    # Parameters
    level = st.slider("Choose recursion depth:", min_value=0, max_value=8, value=5)

    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.axis('off')

    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    p3 = np.array([0.5, np.sqrt(3) / 2])

    sierpinski(ax, p1, p2, p3, level)

    st.pyplot(fig)

if __name__ == "__main__":
    main()
