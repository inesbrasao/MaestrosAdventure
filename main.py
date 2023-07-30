import pygame

import configs
from configs import *
from maestro import Maestro
from platformmanager import PlatformManager
from sheetmanager import SheetManager
from enemymanager import EnemyManager
from lifemanager import Life

def main_game():
    pass

def play():
    pass

def quit():
    pass



pygame.init()

screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
pygame.display.set_caption(Window.TITLE)
pygame.display.set_icon(Window.ICON)

maestro = Maestro()
enemy_manager = EnemyManager()
sheet_manager = SheetManager()
sheet_manager.generate_melody(["DO", "DO", "SOL", "SOL", "LA", "LA", "SOL"])
platform_manager = PlatformManager()
platform_manager.generate_boxes(sheet_manager.get_music_notes())
lives = [
    Life(900),
    Life(930),
    Life(960),
]

clock = pygame.time.Clock()

run = True

while run:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                maestro.jump()

    screen.blit(Img.BACKGROUND, [0, 0])
    life_text = Font.KANIT_30.render(F"Lives:", True, "white")
    screen.blit(life_text, [800, 625])
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        maestro.move("left")
    elif key[pygame.K_RIGHT]:
        maestro.move("right")


    maestro.draw_score(screen)
    maestro.push_down(platform_manager.get_boxes())
    maestro.jumping()
    maestro.draw(screen)
    platform_manager.draw_all(screen)
    maestro.catch_note(sheet_manager.get_music_notes(), sheet_manager.get_melody())
    sheet_manager.draw_all(screen)
    sheet_manager.draw_melody(screen)
    enemy_manager.generate_enemy()
    enemy_manager.draw_all(screen)
    enemy_manager.erase_enemy()
    screen.blit(configs.Img.NO_LIFE, [900, 615])
    screen.blit(configs.Img.NO_LIFE, [930, 615])
    screen.blit(configs.Img.NO_LIFE, [960, 615])
    screen.blit(configs.Img.START, [550, 200])
    screen.blit(configs.Img.QUIT, [550, 330])

    for x in lives:
        x.draw(screen)

        if maestro.gets_hit_by(enemy_manager.get_list_of_enemies()):
            lives.pop()
            print("colisão")
            if len(lives) == 0:
                run = False

    pygame.display.update()

pygame.quit()