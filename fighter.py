from abc import ABC, abstractmethod
from random import randint

RANDOM_MAX = 5

class Weapon(ABC):
    def __init__(self, owner: str):
        self.name = "Оружие"
        self.owner = owner

    @abstractmethod
    def attack(self):
        pass

class Bow(Weapon):
    def __init__(self, owner: str):
        super().__init__(owner)
        self.name = "Лук"

    def attack(self):
        print(f"{self.owner} атаковал Луком")
        return 1

class Sword(Weapon):
    def __init__(self, owner: str):
        super().__init__(owner)
        self.name = "Меч"

    def attack(self):
        print(f"{self.owner} атаковал Мечом")
        return 2

class Laser(Weapon):
    def __init__(self, owner: str):
        super().__init__(owner)
        self.name = "Лазер"

    def attack(self):
        print(f"{self.owner} атаковал Лазером")
        return 3

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon:Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.name}")

    def fight(self):
        return self.weapon.attack()

class Monster:
    def defend(self):
        return randint(1, RANDOM_MAX)

fighter = Fighter("Боец")
monster = Monster()
bow = Bow(fighter.name)
sword = Sword(fighter.name)
laser = Laser(fighter.name)
weapon_list = [bow, sword, laser]

def get_fight_result(weapon_number):
    fighter.changeWeapon(weapon_list[weapon_number-1])
    if fighter.fight() != monster.defend():
        print("**** Боец победил! ****")
        return 1
    else:
        print("**** Монстр победил! ****")
        return -1

def choose_weapon():
    while True:
        try:
            print("1. Лук")
            print("2. Меч")
            print("3. Лазер")
            choice = int(input("Выберите оружие: "))
        except ValueError:
            print("---- Введите число! ----")
            continue
        else:
            if not choice in range(1, len(weapon_list)+1):
                print("---- Такого оружия нет! ----")
                continue
            print()
            return get_fight_result(choice)
        
wins, defeats = 0, 0
while True:
    result = choose_weapon()
    if result > 0:
        wins += 1
    elif result < 0:
        defeats += 1
    print('\n>>>> Счёт: {}-{}'.format(wins, defeats))
    if input('\n****** Сыграете ещё раз? (0-нет, др.клавиша-да): ') == '0':
        break
