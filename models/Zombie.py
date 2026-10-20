from .Enemy import Enemy
from random import choice

class Zombie(Enemy):
    def __init__(self, attack_points, health_points):
        super().__init__("Zombie", attack_points, health_points)

    def talk(self):
        print("Grumbling")

    def spread_disease(self):
        print("The zombie is trying to spread infection")

    def special_ability(self):
        did_special_ability_work = choice([True, False])
        if did_special_ability_work:
            self.health_points += 2
            print("Zombie has cured 2 hp points")
        else:
            print("The zombie failed to use special ability")