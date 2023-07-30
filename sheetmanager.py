import random
import configs
from musicnote import MusicNote


class SheetManager:
    def __init__(self):
        self.__music_notes = []
        self.__melody = []
        self.__music = []

    def get_music_notes(self):
        return self.__music_notes

    def get_melody(self):
        return self.__melody

    def generate_melody(self, list_of_notes):
        x = 220
        for note in list_of_notes:
            self.__melody.append(MusicNote(note, 0))
            self.__music.append(MusicNote(note, 0))

        random.shuffle(list_of_notes)
        for note in list_of_notes:
            self.__music_notes.append(MusicNote(note, x))
            x += 125


    def draw_melody(self, surface):
        count = 0
        for note in self.__melody:
            count += 2
            note.set_x(20 * count)
            note.set_y(610)
            note.draw(surface)

    def draw_all(self, surface):
        for note in self.__music_notes:
            note.draw(surface)







