import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

def modify_sierpinski(depth, length):
    if depth == 1:
        return

    # Define vertices of the triangle
    vertices = np.array([[0, 0], [length, 0], [length / 2, length * np.sqrt(3) / 2]])

    # Choose a random vertex as the starting point
    vertex = vertices[random.randint(0, 2)]

    # Plot the modified Sierpinski triangle
    for _ in range(depth):
        new_vertex = vertices[random.randint(0, 2)]
        vertex = (vertex + new_vertex) / 2
        plt.plot(vertex[0], vertex[1], 'ko', markersize=1)

    # Plot the triangle outline
    for i in range(3):
        plt.plot([vertices[i, 0], vertices[(i + 1) % 3, 0]],
                 [vertices[i, 1], vertices[(i + 1) % 3, 1]], 'k-')

    plt.axis('equal')
    plt.axis('off')

    # Set title
    plt.title("Modified Sierpinski Triangle")

    # Show plot
    st.pyplot()

# Define parameters
depth = st.slider("Depth:", 1, 8, 4)
length = st.slider("Side Length:", 50, 500, 200)

# Draw modified Sierpinski triangle
modify_sierpinski(depth, length)
