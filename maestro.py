import pygame
import configs

class Maestro:
    def __init__(self):
        self.__x = 100
        self.__y = 380
        self.__speed = 5
        self.__jumping_state = None
        self.__on_platform = False
        self.__img = configs.Img.MAESTRO

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value

    def get_on_platform(self):
        return self.__on_platform

    def set_on_platform(self, value):
        self.__on_platform = value

    def get_jumping_state(self):
        return self.__jumping_state

    def set_jumping_state(self, value):
        self.__jumping_state = value

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
        if self.__jumping_state is None:
            return

        if self.__jumping_state == "jump":
            if self.__on_platform:
                self.__y -= self.__speed
                if self.__y <= 220:
                    self.__jumping_state = "fall"
            else:
                self.__y -= self.__speed
                if self.__y <= 280:
                    self.__jumping_state = "fall"

        if self.__jumping_state == "fall":
            if self.__on_platform:
                self.__y += self.__speed
                if self.__y >= 320:
                    self.__jumping_state = None
            else:
                self.__y += self.__speed
                if self.__y >= 380:
                    self.__jumping_state = None


    def jump(self):
        self.__jumping_state = "jump"

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

    def collides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0



