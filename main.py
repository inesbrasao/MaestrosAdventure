import pygame
import configs
from configs import *
from maestro import Maestro
from platformmanager import PlatformManager
from sheetmanager import SheetManager
from enemymanager import EnemyManager
from lifemanager import Life


def main_game(maestro):
    pygame.init()

    screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
    pygame.display.set_caption(Window.TITLE)
    pygame.display.set_icon(Window.ICON)

    clock = pygame.time.Clock()
    run = True

    while run:
        dt = clock.tick(60)

        screen.blit(configs.Img.BACKGROUND, [0, 0])
        start = configs.Img.START.convert_alpha()
        quit = configs.Img.QUIT.convert_alpha()
        screen.blit(start, [550, 200])
        screen.blit(quit, [550, 330])
        start_rect = start.get_rect(topleft=(550, 200))
        quit_rect = quit.get_rect(topleft=(550, 330))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    first_round(maestro)
                elif quit_rect.collidepoint(event.pos):
                    run = False
                    break

        pygame.display.update()

    pygame.quit()


def first_round(maestro):
    pygame.init()

    screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
    pygame.display.set_caption(Window.TITLE)
    pygame.display.set_icon(Window.ICON)

    enemy_manager = EnemyManager()
    melody1 = SheetManager()
    melody1.generate_melody(["DO", "DO", "SOL", "SOL", "LA", "LA", "SOL"])
    platform_manager = PlatformManager()
    platform_manager.generate_boxes(melody1.get_music_notes())
    lives = [
        Life(900),
        Life(930),
        Life(960),
    ]
    maestro.set_score(0)
    maestro.set_x(100)


    clock = pygame.time.Clock()
    run = True

    while run:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
        maestro.catch_note(melody1.get_music_notes(), melody1.get_melody())
        melody1.draw_all(screen)
        melody1.draw_melody(screen)
        enemy_manager.generate_enemy(1)
        enemy_manager.draw_all(screen, 1)
        enemy_manager.erase_enemy()
        screen.blit(configs.Img.NO_LIFE, [900, 615])
        screen.blit(configs.Img.NO_LIFE, [930, 615])
        screen.blit(configs.Img.NO_LIFE, [960, 615])


        for x in lives:
            x.draw(screen)

            if maestro.gets_hit_by(enemy_manager.get_list_of_enemies()):
                lives.pop()
                if len(lives) == 0:
                    game_over(maestro)
                    break

        if melody1.catch_all():
            level_up(maestro, melody1, lives)
            break

        pygame.display.update()


def restart(maestro):
    pygame.init()

    screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
    pygame.display.set_caption(Window.TITLE)
    pygame.display.set_icon(Window.ICON)


    clock = pygame.time.Clock()
    run = True

    while run:
        dt = clock.tick(60)

        screen.blit(configs.Img.BACKGROUND, [0, 0])
        restart = configs.Img.RESTART.convert_alpha()
        quit = configs.Img.QUIT.convert_alpha()
        screen.blit(restart, [550, 200])
        screen.blit(quit, [550, 330])
        maestro.draw_score(screen)
        restart_rect = restart.get_rect(topleft=(550, 200))
        quit_rect = quit.get_rect(topleft=(550, 330))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    first_round(maestro)
                elif quit_rect.collidepoint(event.pos):
                    run = False
                    break

        pygame.display.update()

    pygame.quit()


def level_up(maestro, sheetmanager, lives):
    pygame.init()

    screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
    pygame.display.set_caption(Window.TITLE)
    pygame.display.set_icon(Window.ICON)

    clock = pygame.time.Clock()
    frame_count = 0
    run = True

    while run:
        dt = clock.tick(60)
        frame_count += 1

        screen.blit(configs.Img.BACKGROUND, [0, 0])
        screen.blit(configs.Img.LEVEL_UP, [370, 100])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        sheetmanager.play_melody()

        if frame_count >= 120:
            second_round(maestro, lives)

        pygame.display.update()


def winner(maestro, sheetmanager):
    pygame.init()

    screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
    pygame.display.set_caption(Window.TITLE)
    pygame.display.set_icon(Window.ICON)

    clock = pygame.time.Clock()
    frame_count = 0
    run = True

    while run:
        dt = clock.tick(60)
        frame_count += 1

        screen.blit(configs.Img.BACKGROUND, [0, 0])
        screen.blit(configs.Img.WINNER, [400, 200])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        sheetmanager.play_melody()

        if frame_count >= 120:
            restart(maestro)

        pygame.display.update()


def game_over(maestro):

    pygame.init()

    screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
    pygame.display.set_caption(Window.TITLE)
    pygame.display.set_icon(Window.ICON)

    clock = pygame.time.Clock()
    frame_count = 0
    run = True

    while run:
        dt = clock.tick(60)
        frame_count += 1

        screen.blit(configs.Img.BACKGROUND, [0, 0])
        screen.blit(configs.Img.LOSE, [240, 180])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break


        if frame_count >= 120:
            restart(maestro)

        pygame.display.update()


def second_round(maestro, lives):
    pygame.init()

    screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
    pygame.display.set_caption(Window.TITLE)
    pygame.display.set_icon(Window.ICON)

    enemy_manager = EnemyManager()
    melody2 = SheetManager()
    melody2.generate_melody(["FA", "FA", "MI", "MI", "RE", "RE", "DO"])
    platform_manager = PlatformManager()
    platform_manager.generate_boxes(melody2.get_music_notes())
    maestro.set_x(100)

    clock = pygame.time.Clock()
    run = True

    while run:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
        maestro.catch_note(melody2.get_music_notes(), melody2.get_melody())
        melody2.draw_all(screen)
        melody2.draw_melody(screen)
        enemy_manager.generate_enemy(2)
        enemy_manager.draw_all(screen, 2)
        enemy_manager.erase_enemy()
        screen.blit(configs.Img.NO_LIFE, [900, 615])
        screen.blit(configs.Img.NO_LIFE, [930, 615])
        screen.blit(configs.Img.NO_LIFE, [960, 615])

        for x in lives:
            x.draw(screen)

            if maestro.gets_hit_by(enemy_manager.get_list_of_enemies()):
                lives.pop()
                if len(lives) == 0:
                    game_over(maestro)
                    break

        if melody2.catch_all():
            melody2.play_melody()
            winner(maestro, melody2)
            break

        pygame.display.update()
        

maestro = Maestro()
main_game(maestro)

print("Goodbye!")
