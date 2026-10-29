'''
Cugtas
Latoga
Soriano
9 - Balingkilat
29/10/26
Discussion Activity
'''

class Hero:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def special_move(self):
        print(self.name, "is using", self.weapon)


class Warrior(Hero):
    def special_move(self):
        print(self.name, "swings a", self.weapon)


class Archer(Hero):
    def special_move(self):
        print(self.name, "shoots a", self.weapon)


class Mage(Hero):
    def special_move(self):
        print(self.name, "casts a", self.weapon)


def perform_move(character):
    character.special_move()


warrior = Warrior("Jairo", "mighty sword")
mage = Mage("Audrey", "powerful spell")
archer = Archer("Dianne", "precise arrow")

heroes = [warrior, mage, archer]

for hero in heroes:
    perform_move(hero)
    

