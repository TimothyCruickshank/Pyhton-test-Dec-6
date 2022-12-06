# character class
class Character:
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num

class Hero(Character):
    def __init__(self, level, loot):
        self.level = level
        self.loot = loot

    

class Boss(Character):
    def __init__(self, level, hp, attack_damage, lifespan):
        self.level = level
        self.hp = hp
        self. attack_damage = attack_damage
        self.lifespan = lifespan


hero = Character("Knight", 111), Hero(1, 50.00)
boss = Character("Ogre", 333), Boss(2, 5500, 99, float(Boss.hp/300))


