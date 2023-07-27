import pygame
import configs


class Maestro:
    def __init__(self):
        self.__x = 100
        self.__y = 380
        self.__speed = 5
        self.__jumping_state = None
        self.__on_platform = False
        self.__frame_count = 0
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

    def get_frame_count(self):
        return self.__frame_count

    def set_frame_count(self, value):
        self.__frame_count = value

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
            self.__frame_count += 1
            print(self.__frame_count)
            self.__y -= self.__speed
            if self.__frame_count >= 20:
                self.__jumping_state = "fall"

    def push_down(self, list_of_boxes):
        if self.__jumping_state == "jump":
            return

        print(self.__on_platform)

        self.__y += self.__speed
        for box in list_of_boxes:
            if self.collides_with(box):
                self.__y = 320
                self.__jumping_state = None
                self.__on_platform = True
                self.__frame_count = 0
            elif self.__y >= 380:
                self.__y = 380
                self.__on_platform = False
                self.__jumping_state = None
                self.__frame_count = 0

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

    def catch_note(self, list_of_notes, melody):
        for note in list_of_notes:
            if self.collides_with(note) and (note.get_name() == melody[0].get_name()):
                note.play_sound()
                list_of_notes.remove(note)
                del melody[0]
            elif self.collides_with(note) and (note.get_name() != melody[0].get_name()):
                configs.Sound.BOP.play()

