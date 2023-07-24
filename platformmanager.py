import configs
import box
import sheetmanager

class PlatformManager:
    def __init__(self):
        self.__boxes = []

    def generate_boxes(self, list_of_notes):
        for note in list_of_notes:
            if note.get_y() < 220:
                self.__boxes.append(box.Box(note.get_x()-10))

    def draw_all(self, surface):
        for platform in self.__boxes:
            platform.draw(surface)

    def box_collides_with(self, maestro):
        for platform in self.__boxes:
            #ficar em cima da plataforma
            if maestro.get_jumping_state() == "fall" and platform.collides_with(maestro):
                maestro.set_y(320)
                maestro.set_on_platform(True)
                maestro.set_jumping_state(None)
            # bater contra a plataforma - DIREITA
            elif maestro.get_on_platform() == False and maestro.get_x() > platform.get_x():
                if platform.collides_with(maestro):
                    maestro.set_x(platform.get_x() + 75)
            #bater contra a plataforma - ESQUERDA
            elif maestro.get_on_platform() == False and maestro.get_x() < platform.get_x():
                if platform.collides_with(maestro):
                    maestro.set_x(platform.get_x()-72)
            #descer da plataforma
            elif maestro.get_on_platform():
                if not platform.collides_with(maestro):
                    maestro.set_jumping_state("fall")
                    maestro.set_on_platform(False)




