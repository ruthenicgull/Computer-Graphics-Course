import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Midpoint algorithm for ellipse drawing
def draw_ellipse_midpoint(a, b):
    points = set()
    x = 0
    y = b
    d1 = b * b - a * a * b + 0.25 * a * a
    dx = 2 * b * b * x
    dy = 2 * a * a * y

    while dx < dy:
        points.add((x, y))
        points.add((-x, y))
        points.add((x, -y))
        points.add((-x, -y))

        if d1 < 0:
            x += 1
            dx += 2 * b * b
            d1 += dx + b * b
        else:
            x += 1
            y -= 1
            dx += 2 * b * b
            dy -= 2 * a * a
            d1 += dx - dy + b * b

    d2 = b * b * (x + 0.5) * (x + 0.5) + a * a * (y - 1) * (y - 1) - a * a * b * b

    while y >= 0:
        points.add((x, y))
        points.add((-x, y))
        points.add((x, -y))
        points.add((-x, -y))

        if d2 > 0:
            y -= 1
            dy -= 2 * a * a
            d2 += a * a - dy
        else:
            y -= 1
            x += 1
            dx += 2 * b * b
            dy -= 2 * a * a
            d2 += dx - dy + a * a

    return points

# Function to draw a rotated ellipse using the midpoint algorithm
def draw_rotated_ellipse_midpoint(a, b, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    cos_angle = np.cos(angle_radians)
    sin_angle = np.sin(angle_radians)

    def rotate_point(x, y):
        x_rotated = x * cos_angle - y * sin_angle
        y_rotated = x * sin_angle + y * cos_angle
        return x_rotated, y_rotated

    ellipse_points = draw_ellipse_midpoint(a, b)
    rotated_points = [rotate_point(x, y) for x, y in ellipse_points]

    x_values, y_values = zip(*rotated_points)
    plt.scatter(x_values, y_values, color='black', s=1)

# Function to draw a static square
def draw_static_square(side_length):
    # Define the coordinates of the square
    x_square = np.array([-side_length/2, side_length/2, side_length/2, -side_length/2, -side_length/2])
    y_square = np.array([-side_length/2, -side_length/2, side_length/2, side_length/2, -side_length/2])
    
    # Plot the square
    plt.plot(x_square, y_square, color='red')

# Function to draw a static circle
def draw_static_circle(radius):
    theta = np.linspace(0, 2*np.pi, 100)
    x_circle = radius * np.cos(theta)
    y_circle = radius * np.sin(theta)
    plt.plot(x_circle, y_circle, color='blue')

# Function to update the plot for animation
def update(frame):
    plt.clf()  # Clear the previous plot
    draw_rotated_ellipse_midpoint(800, 400, frame)  # Draw the first ellipse rotating clockwise
    draw_rotated_ellipse_midpoint(400, 800, frame)  # Draw the second ellipse rotating clockwise
    
    draw_static_square(800)  # Draw the static square with side length 200
    draw_static_circle(400)  # Draw the static circle with radius 200
    
    plt.gca().set_aspect('equal', adjustable='box')

# Function to handle the window close event
def on_close(event):
    plt.close()  # Close the plot
    ani.event_source.stop()  # Stop the animation

# Create a blank figure
fig = plt.figure()

# Animate the rotation by continuously updating the plot
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=25)  

# Attach the close event handler
fig.canvas.mpl_connect('close_event', on_close)

plt.show()
