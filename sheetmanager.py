import random

import pygame.time

import configs
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
        self.__music = []
        self.__frames_count = 0

    def get_music_notes(self):
        return self.__music_notes

    def get_melody(self):
        return self.__melody

    def get_music(self):
        return self.__music

    def generate_melody(self, list_of_notes):
        x = 220
        for note in list_of_notes:
            self.__melody.append(MusicNote(note, 0))
            self.__music.append(MusicNote(note, 0))

        random.shuffle(list_of_notes)
        for note in list_of_notes:
            self.__music_notes.append(MusicNote(note, x))
            x += 125

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
        for note in self.__melody:
            note.draw(surface)

    def catch_all(self):
        if len(self.__melody) <= 0:
            return True

    def play_melody(self):
        for note in self.__music:
            self.__frames_count += 1
            if self.__frames_count >= 120:
                note.play_sound()
                self.__frames_count = 0







