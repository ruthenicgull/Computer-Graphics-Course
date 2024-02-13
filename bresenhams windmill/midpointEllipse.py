import matplotlib.pyplot as plt

def draw_ellipse(a, b):
    x0, y0 = 0, b  # Starting point (0, b)
    a_sqr = a * a
    b_sqr = b * b
    d1 = b_sqr - a_sqr * b + 0.25 * a_sqr
    dx = 2 * b_sqr * x0
    dy = 2 * a_sqr * y0

    points = set()

    while dx < dy:
        points.add((x0, y0))
        points.add((-x0, y0))
        points.add((x0, -y0))
        points.add((-x0, -y0))

        if d1 < 0:
            x0 += 1
            dx += 2 * b_sqr
            d1 += dx + b_sqr
        else:
            x0 += 1
            y0 -= 1
            dx += 2 * b_sqr
            dy -= 2 * a_sqr
            d1 += dx - dy + b_sqr

    d2 = b_sqr * (x0 + 0.5) ** 2 + a_sqr * (y0 - 1) ** 2 - a_sqr * b_sqr

    while y0 >= 0:
        points.add((x0, y0))
        points.add((-x0, y0))
        points.add((x0, -y0))
        points.add((-x0, -y0))

        if d2 > 0:
            y0 -= 1
            dy -= 2 * a_sqr
            d2 += a_sqr - dy
        else:
            y0 -= 1
            x0 += 1
            dx += 2 * b_sqr
            dy -= 2 * a_sqr
            d2 += dx - dy + a_sqr

    x_values, y_values = zip(*points)
    plt.scatter(x_values, y_values, color='black', s=1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Example usage:
draw_ellipse(1000, 500)
