import configs
import math
from musicnote import MusicNote
from random import randint

class SheetManager:
    def __init__(self):
        self.__grid = [
            [100, randint(220, 370)], 
            [200, randint(220, 370)],
            [300, randint(220, 370)],
            [400, randint(220, 370)],
            [500, randint(220, 370)],
            [600, randint(220, 370)],
            [700, randint(220, 370)],
            [800, randint(220, 370)],
            [900, randint(220, 370)],
            [1000, randint(220, 370)],
        ]
        self.__music_notes = []
        self.__melody = []
        self.__score = 0

    def get_music_notes(self):
        return self.__music_notes

    def generate_melody(self, list_of_notes):
        count = 0
        for note in list_of_notes:
            count += 2
            for place in self.__grid:
                self.__music_notes.append(MusicNote(note, place[0], place[1]))
                self.__melody.append(MusicNote(note, 20 * count, 610))

    """def draw_melody(self, surface):
        count = 0
        for note in self.__melody:
            count += 2
            note.set_x(20 * count)
            note.set_y(610)
            note.draw(surface)"""

    def draw_all(self, surface):
        for note in self.__music_notes:
            note.draw(surface)

    def play_sound(self, maestro):
        for index, note in enumerate(self.__music_notes):
            #PROBLEMA!!! ou nome da nota == ao nome da nota do index 0 ????
            if index == 0 and maestro.collides_with(note):
                note.play_sound()
                self.__music_notes.remove(note)
            elif index > 0 and maestro.collides_with(note):
                configs.Sound.BOP.play()







