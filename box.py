import pygame
import configs

class Box:
    def __init__(self, x):
        self.__x = x
        self.__y = 450
        self.__img = configs.Img.BOX

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value

    def get_img(self):
        return self.__img


    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def move(self):
        if self.__x <= 200:
            self.__x += 5
        elif self.__x >= 1000:
            self.__x -= 5


    # Area de sobreposição
    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    # Verificar colisão

    def collides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0