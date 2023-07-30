import configs
import pygame


class Life:
    def __init__(self, x):
        self.__x = x
        self.__y = 615
        self.__img = configs.Img.LIFE

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])



