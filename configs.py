import pygame

pygame.init()


class Window:
    WIDTH = 1300
    HEIGHT = 700
    TITLE = "Maestro's Adventure"
    ICON = pygame.image.load("imgs/icon.png")


pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))

class Img:
    START = pygame.image.load("imgs/start.png").convert_alpha()
    RESTART = pygame.image.load("imgs/restart.png").convert_alpha()
    QUIT = pygame.image.load("imgs/quit.png").convert_alpha()
    LEVEL_UP = pygame.image.load("imgs/level.png").convert_alpha()
    WINNER = pygame.image.load("imgs/winner.png").convert_alpha()
    LOSE = pygame.image.load("imgs/lose.png").convert_alpha()
    BACKGROUND = pygame.image.load("imgs/background.png").convert_alpha()
    LIFE = pygame.image.load("imgs/treble.png").convert_alpha()
    NO_LIFE = pygame.image.load("imgs/blacktreble.png").convert_alpha()
    MAESTRO = pygame.image.load("imgs/maestro.png").convert_alpha()
    MAESTRO_LEFT = pygame.transform.flip(MAESTRO, True, False).convert_alpha()
    LIGHT = pygame.image.load("imgs/enemy.png").convert_alpha()
    BOX = pygame.image.load("imgs/box.png").convert_alpha()
    MUSIC_NOTE = {
        "DO": pygame.image.load("imgs/ORANGEnote1.png").convert_alpha(),
        "RE": pygame.image.load("imgs/PINKnote1.png").convert_alpha(),
        "MI": pygame.image.load("imgs/BBLUEnote1.png").convert_alpha(),
        "FA": pygame.image.load("imgs/GREENnote1.png").convert_alpha(),
        "SOL": pygame.image.load("imgs/YELLOWnote1.png").convert_alpha(),
        "LA": pygame.image.load("imgs/REDnote1.png").convert_alpha(),
    }

class Sound:
    MUSIC_NOTE = {
        "DO": pygame.mixer.Sound("sounds/do.ogg"),
        "RE": pygame.mixer.Sound("sounds/re.ogg"),
        "MI": pygame.mixer.Sound("sounds/mi.ogg"),
        "FA": pygame.mixer.Sound("sounds/fa.ogg"),
        "SOL": pygame.mixer.Sound("sounds/sol.ogg"),
        "LA": pygame.mixer.Sound("sounds/la.ogg"),
    }
    BOP = pygame.mixer.Sound("sounds/bop.ogg")

class Font:
    KANIT_30 = pygame.font.Font("fonts/Kanit-Medium.ttf", 30)

