import pygame
import configs

class Box:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = configs.Img.BOX

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])


    # Area de sobreposição
    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    # Verificar colisão

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0