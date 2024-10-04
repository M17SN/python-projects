import pygame

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))  # Red color for bullets
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)
