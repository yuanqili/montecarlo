import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Monte Carlo simulation for estimating Pi')

with st.expander('🧠 How it works'):
    st.markdown(r'''
    This is a simple Monte Carlo simulation for estimating the value of $\pi$.
    The method is as follows:
    - Draw a square with side length $\ell$ and inscribe a circle with radius $r = \ell/2$.
    - Randomly sample $n$ points in the square.
    - The ratio of points in the circle to the total number of points is an estimate of the ratio of the area of the circle to the area of the square.
        $$
            \frac{\text{\# Points in circle}}{\text{\# Total points}}
            \approx \frac{\text{Area of circle}}{\text{Area of square}}
            = \frac{\pi r^2}{\ell^2}
            = \frac{\pi (\ell/2)^2}{\ell^2}
            = \frac{\pi}{4}
        $$
    - Therefore,
        $$
            \pi \approx 4 \times \frac{\text{\# Points in circle}}{\text{\# Total points}}
        $$ 
    ''')

# parameters
side_length = 10.0
radius = side_length / 2
center_x = side_length / 2
center_y = side_length / 2
num_points = 1000

# parameters
with st.sidebar:
    side_length = st.slider('Side length of the square ($\ell$)', 1.0, 10.0, 1.0)
    radius = st.slider('Radius of the circle ($r = \ell / 2$)', 0.5, 10.0, side_length / 2, disabled=True)
    center_x = side_length / 2
    center_y = side_length / 2
    num_points = st.number_input('Number of points ($n$)', 1, 100000, 1000)

# draw random samples of points in the square
xs = np.random.uniform(0, side_length, num_points)
ys = np.random.uniform(0, side_length, num_points)

# determine if each point is inside the circle
num_inside = 0
inside_xs, inside_ys = [], []
outside_xs, outside_ys = [], []
for point_no in range(num_points):
    # the coordinate of the point
    x, y = xs[point_no], ys[point_no]
    # distance to the center of the circle
    dist = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    # check if the point is inside the circle
    if dist <= radius:
        num_inside += 1
        inside_xs.append(x)
        inside_ys.append(y)
    else:
        outside_xs.append(x)
        outside_ys.append(y)

# estimate pi
pi = 4 * num_inside / num_points
error = (pi - np.pi) / np.pi

columns = st.columns(2)
with columns[0]:
    st.metric(label='Real value of $\pi$', value=round(np.pi, 6))
with columns[1]:
    st.metric(label='Estimated value of $\pi$', value=round(pi, 6), delta=f'{error:.4%}')

# plot the points
fig, ax = plt.subplots(figsize=(6, 6))

# draw a circle
circle = plt.Circle((center_x, center_y), radius, color='r', fill=False)
ax.add_artist(circle)

# plots the points
ax.scatter(inside_xs, inside_ys, s=1, c='g')
ax.scatter(outside_xs, outside_ys, s=1, c='b')

# figure configurations
ax.set_xlim(0, side_length)
ax.set_ylim(0, side_length)
ax.set_aspect('equal')
ax.set_title('Monte Carlo simulation for estimating $\pi$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# displays the figure
st.pyplot(fig)
