import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to draw a rotated ellipse
def draw_rotated_ellipse(a, b, angle_degrees, direction):
    # Generate points for an unrotated ellipse
    t = np.linspace(0, 2*np.pi, 100)
    x_unrotated = a * np.cos(t)
    y_unrotated = b * np.sin(t)

    # Rotate the ellipse points
    angle_radians = np.radians(angle_degrees)
    if direction == 'clockwise':
        angle_radians *= -1  # Reverse direction if clockwise
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                                [np.sin(angle_radians), np.cos(angle_radians)]])
    xy_rotated = np.dot(rotation_matrix, np.vstack([x_unrotated, y_unrotated]))

    # Plot the rotated ellipse
    plt.plot(xy_rotated[0], xy_rotated[1], color='black')

# Function to draw a static circle
def draw_static_circle(radius):
    # Draw a static circle
    circle = plt.Circle((0, 0), radius, color='blue', fill=False)
    plt.gca().add_artist(circle)

# Function to draw a static square
def draw_static_square(side_length):
    # Define the coordinates of the square
    x_square = np.array([-side_length/2, side_length/2, side_length/2, -side_length/2, -side_length/2])
    y_square = np.array([-side_length/2, -side_length/2, side_length/2, side_length/2, -side_length/2])
    
    # Plot the square
    plt.plot(x_square, y_square, color='red')

# Function to update the plot for animation
def update(frame):
    plt.clf()  # Clear the previous plot
    draw_rotated_ellipse(800, 400, frame, 'clockwise')  # Draw the first ellipse rotating clockwise
    draw_rotated_ellipse(800, 400, frame, 'anticlockwise')  # Draw the second ellipse rotating anticlockwise
    
    draw_static_circle(400)  # Draw the static circle with radius 100
    draw_static_square(800)  # Draw the static square with side length 200
    
    plt.gca().set_aspect('equal', adjustable='box')

# Function to handle the window close event
def on_close(event):
    plt.close()  # Close the plot

# Create a blank figure
fig = plt.figure()

# Animate the rotation by continuously updating the plot
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=25)  

# Attach the close event handler
fig.canvas.mpl_connect('close_event', on_close)

plt.show()
