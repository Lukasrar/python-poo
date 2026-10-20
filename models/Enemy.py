class Enemy:
    def __init__(self, type_of_enemy: str = "Unknown", health_points: int = 100, attack_points: int = 10):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_points = attack_points

    def talk(self):
        print(f"The {self.__type_of_enemy} says: 'Grrr!' Prepare to fight!")

    def walk_forward(self):
        print(f"The {self.__type_of_enemy} walks forward, ready to attack!")

    def attack(self):
        print(f"The {self.__type_of_enemy} attacks with {self.attack_points} attack points!")

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def special_ability(self):
        print(f"The {self.__type_of_enemy} does not have a special ability defined.")
