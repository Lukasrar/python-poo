from models.Enemy import Enemy
from models.Hero import *
from models.Weapon import *

def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:

        print('---------')
        print(f'Hero has {hero.health_points} HP')
        print(f'Enemy ({enemy.get_type_of_enemy()}) has {enemy.health_points} HP')

        enemy.attack()
        hero.health_points -= enemy.attack_points
        hero.attack()
        enemy.health_points -= hero.attack_damage

    print('---------')

    if hero.health_points > 0:
        print(f'Hero wins')
    else:
        print(f'{enemy.get_type_of_enemy()} wins')
        
  
