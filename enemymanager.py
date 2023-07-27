import configs
from enemy import Light


class EnemyManager:
    def __init__(self):
        self.__list_of_enemies = []
        self.__frame_count = 0

    def generate_enemy(self):
        self.__frame_count += 1
        if self.__frame_count == 200:
            self.__frame_count = 0
            self.__list_of_enemies.append(Light())

    def draw_all(self, surface):
        self.generate_enemy()
        for enemy in self.__list_of_enemies:
            enemy.draw(surface)
            enemy.move()

    def erase_enemy(self, maestro):
        for enemy in self.__list_of_enemies:
            if enemy.collides_with(maestro):
                self.__list_of_enemies.remove(enemy)
            elif enemy.get_y() > 570:
                self.__list_of_enemies.remove(enemy)





