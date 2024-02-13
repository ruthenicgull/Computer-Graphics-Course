import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Hollow Ellipse")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the ellipse parameters
ellipse_center = (width // 2, height // 2)
ellipse_width = 200
ellipse_height = 100
ellipse_thickness = 5  # Thickness of the ellipse border
angle = 0
rotation_speed = 2  # in degrees per frame

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Calculate the new angle of rotation
    angle += rotation_speed
    if angle >= 360:
        angle -= 360

    # Calculate the rotated ellipse surface
    rotated_ellipse_outer = pygame.Surface((ellipse_width, ellipse_height), pygame.SRCALPHA)
    rotated_ellipse_outer.fill((0, 0, 0, 0))  # Fill with transparent color
    pygame.draw.ellipse(rotated_ellipse_outer, BLACK, (0, 0, ellipse_width, ellipse_height), ellipse_thickness)

    # Calculate the rotated ellipse surface for inner boundary
    rotated_ellipse_inner = pygame.Surface((ellipse_width, ellipse_height), pygame.SRCALPHA)
    rotated_ellipse_inner.fill((0, 0, 0, 0))  # Fill with transparent color
    pygame.draw.ellipse(rotated_ellipse_inner, WHITE, (ellipse_thickness, ellipse_thickness, ellipse_width - 2 * ellipse_thickness, ellipse_height - 2 * ellipse_thickness))

    # Rotate the ellipses
    rotated_ellipse_outer = pygame.transform.rotate(rotated_ellipse_outer, angle)
    rotated_ellipse_inner = pygame.transform.rotate(rotated_ellipse_inner, angle)

    # Get the rectangles enclosing the rotated ellipses
    rotated_rect_outer = rotated_ellipse_outer.get_rect()
    rotated_rect_inner = rotated_ellipse_inner.get_rect()

    # Set the centers of the rectangles to match the center of the original ellipse
    rotated_rect_outer.center = ellipse_center
    rotated_rect_inner.center = ellipse_center

    # Draw the rotated ellipses onto the screen
    screen.blit(rotated_ellipse_outer, rotated_rect_outer.topleft)
    screen.blit(rotated_ellipse_inner, rotated_rect_inner.topleft)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)
