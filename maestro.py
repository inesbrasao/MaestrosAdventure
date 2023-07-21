import pygame
import configs

class Maestro:
    def __init__(self):
        self.__x = 100
        self.__y = 380
        self.__speed = 5
        self.__state = None
        self.__img = configs.Img.MAESTRO

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def move(self, direction):
        if direction == "right":
            self.__x += self.__speed
            self.__img = configs.Img.MAESTRO
        elif direction == "left":
            self.__x -= self.__speed
            self.__img = configs.Img.MAESTRO_LEFT

        self.limit_boundaries()

    def jumping(self):
        if self.__state is None:
            return

        if self.__state == "jump":
            self.__y -= self.__speed
            if self.__y <= 280:
                self.__state = "fall"

        if self.__state == "fall":
            self.__y += self.__speed
            if self.__y >= 380:
                self.__state = None


    def jump(self):
        self.__state = "jump"

    def limit_boundaries(self):
        if self.__x < 100:
            self.__x = 100
        elif self.__x > 1100:
            self.__x = 1100

    # Area de sobreposição
    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    # Verificar colisão

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0
