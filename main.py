# from models import Dog

# dog = Dog()


# print(dog.legs)
# print(dog.ears)
# print(dog.type)
# print(dog.color)


# from models.Enemy import Enemy
from models.Zombie import Zombie
from models.Ogre import Ogre
# from utils.Battle import battle
from utils.HeroBattle import *
from models.Hero import *
from models.Weapon import *
zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
hero = Hero(10, 1)

# print(zombie.get_type_of_enemy())
# print(zombie.talk())
# print(zombie.spread_disease())

# print(ogre.get_type_of_enemy())
# print(ogre.talk())


# battle(zombie)
# battle(ogre)

# battle(zombie, ogre)


weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero, zombie)
# enemy = Enemy("Goblin", 150, 20)

# enemy.talk()
# enemy.walk_forward()
# enemy.attack()

# print(enemy.get_type_of_enemy())

