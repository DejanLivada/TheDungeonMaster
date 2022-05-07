import pygame


class Platform:
    def __init__(self, rect: pygame.Rect):
        self.rect: pygame.Rect = rect

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)
