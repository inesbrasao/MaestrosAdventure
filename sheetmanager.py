import configs
from musicnote import MusicNote

class SheetManager:
    def __init__(self):
        self.__music_notes = []
        self.__score = 0


    def generate_melody(self, list_of_notes):
        for note in list_of_notes:
            self.__music_notes.append(MusicNote(note))

    def draw_all(self, surface):
        for note in self.__music_notes:
            note.draw(surface)

    def play_sound(self, maestro):
        for note in self.__music_notes:
            if maestro.colides_with(note):
                note.play_sound()



