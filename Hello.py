import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def modify_sierpinski(ax, x, y, length, depth):
    if depth == 0:
        points = np.array([[x, y], [x + length / 2, y + length], [x + length, y]])
        ax.fill(points[:, 0], points[:, 1], 'k')
    else:
        modify_sierpinski(ax, x, y, length / 2, depth - 1)
        modify_sierpinski(ax, x + length / 2, y, length / 2, depth - 1)
        modify_sierpinski(ax, x + length / 4, y + length / 2, length / 2, depth - 1)

def main():
    st.title('Sierpinski Triangle')
    st.sidebar.header('Parameters')
    depth = st.sidebar.slider('Depth', min_value=1, max_value=7, value=3)
    length = st.sidebar.slider('Length', min_value=50, max_value=500, value=300)
    st.write('Adjust the parameters in the sidebar to change the Sierpinski triangle.')

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim([0, length])
    ax.set_ylim([0, length])
    ax.axis('off')

   fig= modify_sierpinski(ax, 0, 0, length, depth)

    st.pyplot(fig)

if __name__ == '__main__':
    main()
