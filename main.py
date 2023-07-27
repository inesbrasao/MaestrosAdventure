import pygame
from configs import *
from maestro import Maestro
from platformmanager import PlatformManager
from sheetmanager import SheetManager
from enemymanager import EnemyManager

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
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        maestro.move("left")
    elif key[pygame.K_RIGHT]:
        maestro.move("right")

    maestro.push_down(platform_manager.get_boxes())
    maestro.jumping()
    maestro.draw(screen)
    platform_manager.draw_all(screen)
    maestro.catch_note(sheet_manager.get_music_notes(), sheet_manager.get_melody())
    sheet_manager.draw_all(screen)
    sheet_manager.draw_melody(screen)
    enemy_manager.generate_enemy()
    enemy_manager.draw_all(screen)
    enemy_manager.erase_enemy(maestro)


    pygame.display.update()

pygame.quit()