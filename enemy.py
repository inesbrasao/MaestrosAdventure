import configs
import random
import pygame


class Light:
    def __init__(self):
        self.__x = random.randint(200, 1000)
        self.__y = 0
        self.__speed = 7
        self.__img = configs.Img.LIGHT
        self.__sound = 0

    def get_y(self):
        return self.__y

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def move(self):
        self.__y += self.__speed

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    # Verificar colisão

    def collides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0