import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Ellipse")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the ellipse parameters
ellipse_center = (width // 2, height // 2)
ellipse_width = 200
ellipse_height = 100
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
    rotated_ellipse = pygame.Surface((ellipse_width, ellipse_height), pygame.SRCALPHA)
    rotated_ellipse.fill((0, 0, 0, 0))  # Fill with transparent color
    pygame.draw.ellipse(rotated_ellipse, BLACK, (0, 0, ellipse_width, ellipse_height))

    # Rotate the ellipse
    rotated_ellipse = pygame.transform.rotate(rotated_ellipse, angle)

    # Get the rectangle enclosing the rotated ellipse
    rotated_rect = rotated_ellipse.get_rect()

    # Set the center of the rectangle to match the center of the original ellipse
    rotated_rect.center = ellipse_center

    # Draw the rotated ellipse onto the screen
    screen.blit(rotated_ellipse, rotated_rect.topleft)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)
