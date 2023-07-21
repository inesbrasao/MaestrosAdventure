import configs
import math
from musicnote import MusicNote

class SheetManager:
    def __init__(self):
        self.__music_notes = []
        self.__melody = []
        self.__score = 0

    def get_music_notes(self):
        return self.__music_notes

    def generate_melody(self, list_of_notes):
        for note in list_of_notes:
            self.__music_notes.append(MusicNote(note))
            self.__melody.append(MusicNote(note))

    def draw_melody(self, surface):
        count = 0
        for note in self.__melody:
            count += 2
            note.set_x(30 * count)
            note.set_y(630)
            note.draw(surface)


    def draw_all(self, surface):
        for note in self.__music_notes:
            note.draw(surface)

    def play_sound(self, maestro):
        for note in self.__music_notes:
            if maestro.colides_with(note):
                note.play_sound()



