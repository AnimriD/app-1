import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

def modify_sierpinski(depth, length):
    if depth == 0:
        return

    # Define vertices of the triangle
    vertices = np.array([[0, 0], [length, 0], [length / 2, length * np.sqrt(3) / 2]])

    # Choose a random vertex as the starting point
    vertex = vertices[random.randint(0, 2)]

    # Create Matplotlib figure and axis
    fig, ax = plt.subplots()

    # Plot the modified Sierpinski triangle
    for _ in range(depth):
        new_vertex = vertices[random.randint(0, 2)]
        vertex = (vertex + new_vertex) / 2
        ax.plot(vertex[0], vertex[1], 'ko', markersize=1)

    # Plot the triangle outline
    for i in range(3):
        ax.plot([vertices[i, 0], vertices[(i + 1) % 3, 0]],
                 [vertices[i, 1], vertices[(i + 1) % 3, 1]], 'k-')

    ax.axis('equal')
    ax.axis('off')

    # Set title
    ax.set_title("Modified Sierpinski Triangle")

    # Show plot
    st.pyplot(fig)

# Define parameters
depth = st.slider("Depth:", 1, 8, 4)
length = st.slider("Side Length:", 50, 500, 200)

# Draw modified Sierpinski triangle
modify_sierpinski(depth, length)
