import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Bresenham's circle drawing algorithm
def draw_circle(radius):
    x = 0
    y = radius
    d = 3 - 2 * radius
    points = set()

    while x <= y:
        points.add((x, y))
        points.add((-x, y))
        points.add((x, -y))
        points.add((-x, -y))
        points.add((y, x))
        points.add((-y, x))
        points.add((y, -x))
        points.add((-y, -x))

        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

# Function for ellipse drawing
def draw_ellipse(a, b):
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
def draw_rotated_ellipse(a, b, angle_degrees, direction):
    angle_radians = np.radians(angle_degrees)
    if direction == 'clockwise':
        angle_radians *= -1  # Reverse direction if clockwise
    cos_angle = np.cos(angle_radians)
    sin_angle = np.sin(angle_radians)

    def rotate_point(x, y):
        x_rotated = x * cos_angle - y * sin_angle
        y_rotated = x * sin_angle + y * cos_angle
        return x_rotated, y_rotated

    ellipse_points = draw_ellipse(a, b)
    rotated_points = [rotate_point(x, y) for x, y in ellipse_points]

    x_values, y_values = zip(*rotated_points)
    plt.scatter(x_values, y_values, color='black', s=1)

# Function to draw a static square
def draw_square(side_length):
    # Define the coordinates of the square
    x_square = np.array([-side_length/2, side_length/2, side_length/2, -side_length/2, -side_length/2])
    y_square = np.array([-side_length/2, -side_length/2, side_length/2, side_length/2, -side_length/2])
    
    # Plot the square
    plt.plot(x_square, y_square, color='red')

# Function to update the plot for animation
def update(frame):
    plt.clf()  # Clear the previous plot
    draw_rotated_ellipse(800, 200, frame, 'anticlockwise')  # Draw the first ellipse rotating anticlockwise
    draw_rotated_ellipse(800, 200, frame, 'clockwise')  # Draw the second ellipse rotating clockwise
    
    # Draw the static circle using Bresenham's algorithm
    circle_points = draw_circle(200)
    x_circle, y_circle = zip(*circle_points)
    plt.scatter(x_circle, y_circle, color='blue', s=1)

    draw_square(400)  # Draw the static square with side length 200
    
    plt.gca().set_aspect('equal', adjustable='box')

# Create a blank figure
fig = plt.figure()

# Animate the rotation by continuously updating the plot
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=5)  

plt.show()
