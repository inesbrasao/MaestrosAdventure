import pygame
from configs import *
from maestro import Maestro
from sheetmanager import SheetManager

pygame.init()

screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
pygame.display.set_caption(Window.TITLE)
pygame.display.set_icon(Window.ICON)

maestro = Maestro()
sheet_manager = SheetManager()
sheet_manager.generate_melody(["DO", "DO", "SOL", "SOL", "LA", "LA", "SOL"])
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

    maestro.jumping()
    maestro.draw(screen)
    sheet_manager.play_sound(maestro)
    sheet_manager.draw_all(screen)

    pygame.display.update()

pygame.quit()