import configs
from enemy import Light


class EnemyManager:
    def __init__(self):
        self.__list_of_enemies = []
        self.__frame_count = 0

    def get_list_of_enemies(self):
        return self.__list_of_enemies

    def generate_enemy(self, round):
        self.__frame_count += 1
        if round == 1 and self.__frame_count >= 150:
            self.__frame_count = 0
            self.__list_of_enemies.append(Light())
        elif round == 2 and self.__frame_count >= 100:
            self.__frame_count = 0
            self.__list_of_enemies.append(Light())

    def draw_all(self, surface, round):
        self.generate_enemy(round)
        for enemy in self.__list_of_enemies:
            enemy.draw(surface)
            enemy.move()

    def erase_enemy(self):
        for enemy in self.__list_of_enemies:
            if enemy.get_y() > 570:
                self.__list_of_enemies.remove(enemy)





