# Your RPG Hero

class hero: #class
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def take_damage(self, amount):
        self.hp -= amount
        print(self.name, "took", amount, "points of damage.")
        print("Your hero", self.name, "has", self.hp, "hp left.")


#1st hero (Arthur)
name1 = "Arthur"
hp1 = 100

myHero1 = hero(name1, hp1)
myHero1.take_damage(10)

#2nd hero (Morgana)
name2 = "Morgana"
hp2 = 100

myHero2 = hero(name2, hp2)
myHero2.take_damage(0)
