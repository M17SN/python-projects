
import pygame

# Player spaceship class
class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Green color for the player
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def update(self, keys):
        # Move left
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        # Move right
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Keep the player within the screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

    def draw(self, screen):
        screen.blit(self.image, self.rect)
