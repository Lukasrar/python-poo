from random import choice

from .Enemy import Enemy

class Ogre(Enemy):
    def __init__(self, attack_points, health_points):
        super().__init__("Ogre")
        self.health_points = health_points
        self.attack_points = attack_points

    def talk(self):
        print(f"Ogre is slamming the ground and growling")

    def special_ability(self):
        did_special_ability_work = choice([True, False])
        if did_special_ability_work:
            self.attack_points += 5
            print("Ogre has increased its attack points by 5")
        else:
            print("The ogre failed to use special ability")