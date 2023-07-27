import box


class PlatformManager:
    def __init__(self):
        self.__boxes = []

    def get_boxes(self):
        return self.__boxes

    def generate_boxes(self, list_of_notes):
        for note in list_of_notes:
            if note.get_y() < 220:
                self.__boxes.append(box.Box(note.get_x()-10))

    def draw_all(self, surface):
        for platform in self.__boxes:
            platform.draw(surface)






