import pygame

pygame.init()

class Window:
    WIDTH = 1300
    HEIGHT = 700
    TITLE = "Maestro's Adventure"
    ICON = pygame.image.load("imgs/icon.png")

class Img:
    START = pygame.image.load("imgs/start.png")
    RESTART = pygame.image.load("imgs/restart.png")
    QUIT = pygame.image.load("imgs/quit.png")
    BACKGROUND = pygame.image.load("imgs/background.png")
    LIFE = pygame.image.load("imgs/treble.png")
    NO_LIFE = pygame.image.load("imgs/blacktreble.png")
    MAESTRO = pygame.image.load("imgs/maestro.png")
    MAESTRO_LEFT = pygame.transform.flip(MAESTRO, True, False)
    LIGHT = pygame.image.load("imgs/enemy.png")
    BOX = pygame.image.load("imgs/box.png")
    MUSIC_NOTE = {
        "DO": pygame.image.load("imgs/ORANGEnote1.png"),
        "RE": pygame.image.load("imgs/PINKnote.png"),
        "MI": pygame.image.load("imgs/BBLUEnote.png"),
        "FA": pygame.image.load("imgs/GREENnote.png"),
        "SOL": pygame.image.load("imgs/YELLOWnote1.png"),
        "LA": pygame.image.load("imgs/REDnote1.png"),
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

