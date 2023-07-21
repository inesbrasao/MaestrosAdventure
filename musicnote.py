import random
import pygame
import configs

class MusicNote:
    def __init__(self, name):
        self.__name = name
        self.__x = random.randint(220, 1030)
        self.__y = random.randint(100, 180)
        self.__img = configs.Img.MUSIC_NOTE[name]
        self.__sound = configs.Sound.MUSIC_NOTE[name]

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def play_sound(self):
        self.__sound.play()
        self.__sound.set_volume(1)

    # Area de sobreposição
    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    # Verificar colisão

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0