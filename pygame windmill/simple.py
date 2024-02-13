import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the ball
ball_radius = 50
ball_color = (255, 0, 0)  # Red
ball_pos = [width // 2, height // 2]
ball_velocity = [5, 5]

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Check for collisions with walls
    if ball_pos[0] + ball_radius >= width or ball_pos[0] - ball_radius <= 0:
        ball_velocity[0] *= -1
    if ball_pos[1] + ball_radius >= height or ball_pos[1] - ball_radius <= 0:
        ball_velocity[1] *= -1

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)
