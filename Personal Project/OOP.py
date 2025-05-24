import random

class Hero:
    def __init__(self, name, health, armor, power, new):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.new = new

    def info(self):
        print(self.name, self.health, self.armor, self.power, self.new)
        
    def alive(self):
        if self.health == 0:
            print("your hero is dead.")

    def strike(self, enemy):
        if enemy.armor <= 0:
            enemy.health = enemy.health - self.power
            if enemy.health < 0:
                enemy.health = 0
        else:
            enemy.armor = enemy.armor - self.power
            if enemy.armor < 0:
                enemy.armor = 0
        print(enemy.name, "has", enemy.armor, "armour left and", enemy.health, "health left.")

    def chance(self, enemy):
        chance_turn = random.randint(1, 2)
        if chance_turn == 1:
            self.strike(enemy)
        else:
            enemy.strike(self)

class Rascal(Hero):
    def __init__(self, name, health, armor, power, new):
        super().__init__(name, health, armor, power, new)

    def super_strike(self, enemy):
        super().strike(enemy)
        super().strike(enemy)

    def chance(self, enemy):
        super().chance(enemy)
        super().chance(enemy)

class Warrior(Hero):
    def __init__(self, name, health, armor, power, new):
        super().__init__(name, health, armor, power, new)

    def super_strike(self, enemy):
        super().strike(enemy)
        super().strike(enemy)

    def chance(self, enemy):
        super().chance(enemy)
        super().chance(enemy)

class Dragon(Hero):
    def __init__(self, name, health, armor, power, new):
        super().__init__(name, health, armor, power, new)

    def super_strike(self, enemy):
        super().strike(enemy)
        super().strike(enemy)

    def chance(self, enemy):
        super().chance(enemy)
        super().chance(enemy)



Warrior = Warrior("Knight", 120, 50, 30, True)
Rascal_1 = Rascal("Peter", 80, 5, 10, True)
Rascal_2 = Rascal("Sergio", 80, 5, 10, True)
Dragon_1 = Dragon("Drogon", 100, 5, 15, True)
Dragon_2 = Dragon("Viserion", 100, 5, 15, True)

step = 0

while step < 20:
    print("You have travelled", step, "steps")
    step = step + 1
    chance_rascal = random.randint(1, 5)
    if chance_rascal == 1:
        choice = input("Do you want to approach this opponent? y - yes, n - no")
        if choice == "y":
            Warrior.chance(Rascal_1)





