import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def sierpinski(x, y, length, depth):
    if depth == 0:
        return
    h = length * np.sqrt(3) / 2
    points = np.array([[x, y], [x + length / 2, y + h], [x + length, y]])
    plt.fill(points[:, 0], points[:, 1], 'k')
    sierpinski(x, y, length / 2, depth - 1)
    sierpinski(x + length / 2, y, length / 2, depth - 1)
    sierpinski(x + length / 4, y + h / 2, length / 2, depth - 1)

def main():
    st.title('Sierpinski Triangle')
    st.sidebar.header('Parameters')
    depth = st.sidebar.slider('Depth', min_value=1, max_value=7, value=3)
    length = st.sidebar.slider('Length', min_value=50, max_value=500, value=300)
    st.write('Adjust the parameters in the sidebar to change the Sierpinski triangle.')

    # Draw Sierpinski triangle
    plt.figure(figsize=(6, 6))
    plt.axis('off')
    sierpinski(0, 0, length, depth)
    st.pyplot()

if __name__ == '__main__':
    main()
