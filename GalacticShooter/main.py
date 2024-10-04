
import pygame
from player import Player

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Create the player object and bullets list
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
bullets_in_screen = []
# Game loop variables
running = True

# Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keys for player movement
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Fill screen with black background
    screen.fill((0, 0, 0))

    # update bullets' position
    for bullet in bullets_in_screen:
        bullet.rect.y -= bullet.speed  # Move bullet upward

    # Draw the player and bullets
    player.draw(screen)
    for bullet in bullets_in_screen:
        bullet.draw(screen)
    # Update the display
    pygame.display.flip()

    bullets = [bullet for bullet in bullets_in_screen if bullet.rect.bottom > 0]

    
    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
