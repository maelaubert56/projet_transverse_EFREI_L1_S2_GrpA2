import pygame
import DEFAULT
import random


class Ground(pygame.sprite.Sprite):

    def __init__(self):
        self.i = random.randint(0, len(DEFAULT.path_terrain)-1)
        pygame.sprite.Sprite.__init__(self)

        # on importe l'arrière-plan et on redimensionne l'image
        self.image = pygame.image.load(DEFAULT.path_terrain[self.i])
        self.rect = self.image.get_rect()
        self.rect.width = DEFAULT.window_width
        DEFAULT.height = DEFAULT.window_width * self.rect.height / self.rect.width
        self.rect.height = DEFAULT.window_height
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.mask = pygame.mask.from_surface(self.image)

    def change_background(self):
        self.i = (self.i+1)%len(DEFAULT.path_terrain)
        # on importe l'arrière-plan et on redimensionne l'image
        self.image = pygame.image.load(DEFAULT.path_terrain[self.i])
        self.rect = self.image.get_rect()
        self.rect.width = DEFAULT.window_width
        DEFAULT.height = DEFAULT.window_width * self.rect.height / self.rect.width
        self.rect.height = DEFAULT.window_height
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.mask = pygame.mask.from_surface(self.image)

