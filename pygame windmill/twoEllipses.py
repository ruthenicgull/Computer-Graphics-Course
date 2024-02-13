import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_rotating_hollow_ellipse(screen, center, width, height, thickness, rotation_angle):
    # Calculate the rotated ellipse surface for outer boundary
    rotated_ellipse_outer = pygame.Surface((width, height), pygame.SRCALPHA)
    rotated_ellipse_outer.fill((0, 0, 0, 0))  # Fill with transparent color
    pygame.draw.ellipse(rotated_ellipse_outer, BLACK, (0, 0, width, height), thickness)

    # Calculate the rotated ellipse surface for inner boundary
    rotated_ellipse_inner = pygame.Surface((width, height), pygame.SRCALPHA)
    rotated_ellipse_inner.fill((0, 0, 0, 0))  # Fill with transparent color
    pygame.draw.ellipse(rotated_ellipse_inner, WHITE, (thickness, thickness, width - 2 * thickness, height - 2 * thickness))

    # Rotate the ellipses
    rotated_ellipse_outer = pygame.transform.rotate(rotated_ellipse_outer, rotation_angle)
    rotated_ellipse_inner = pygame.transform.rotate(rotated_ellipse_inner, rotation_angle)

    # Get the rectangles enclosing the rotated ellipses
    rotated_rect_outer = rotated_ellipse_outer.get_rect()
    rotated_rect_inner = rotated_ellipse_inner.get_rect()

    # Set the centers of the rectangles to match the center of the original ellipse
    rotated_rect_outer.center = center
    rotated_rect_inner.center = center

    # Draw the rotated ellipses onto the screen
    screen.blit(rotated_ellipse_outer, rotated_rect_outer.topleft)
    screen.blit(rotated_ellipse_inner, rotated_rect_inner.topleft)

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Hollow Ellipses")

# Set initial rotation angles for both ellipses
angle1 = 0
angle2 = 180  # Start the second ellipse at 180 degrees to ensure it rotates in the opposite direction

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Call the function to draw the first rotating hollow ellipse
    draw_rotating_hollow_ellipse(screen, (width // 2, height // 2), 200, 100, 5, angle1)

    # Call the function to draw the second rotating hollow ellipse
    draw_rotating_hollow_ellipse(screen, (width // 2, height // 2), 200, 100, 5, angle2)

    # Update the display
    pygame.display.flip()

    # Increment the rotation angles
    angle1 += 2
    angle2 -= 2

    # Ensure the angles stay within the range 0-359 degrees
    angle1 %= 360
    angle2 %= 360

    # Set the frame rate
    pygame.time.Clock().tick(60)
