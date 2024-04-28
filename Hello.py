import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

<<<<<<< HEAD
def modify_sierpinski(ax, x, y, length, depth):
    if depth == 1:
        points = np.array([[x, y], [x + length / 2, y + length], [x + length, y]])
        ax.fill(points[:, 0], points[:, 1], 'k')
    else:
        modify_sierpinski(ax, x, y, length / 2, depth - 1)
        modify_sierpinski(ax, x + length / 2, y, length / 2, depth - 1)
        modify_sierpinski(ax, x + length / 4, y + length / 2, length / 2, depth - 1)
=======
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
>>>>>>> e3f737bcc3a2e02eef8ad49b8e801010796c058c


<<<<<<< HEAD
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim([0, length])
    ax.set_ylim([0, length])
    ax.axis('off')

    modify_sierpinski(ax, 0, 0, length, depth)

    st.pyplot(fig)
=======
progress_bar.empty()
>>>>>>> e3f737bcc3a2e02eef8ad49b8e801010796c058c

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
