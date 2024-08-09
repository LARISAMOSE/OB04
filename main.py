from abc import ABC, abstractmethod

# Шаг 1: Создаем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."

class Axe(Weapon):
    def attack(self):
        return "Боец размахивает топором."

# Шаг 3: Модифицируем класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__}.")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print(f"{self.name} безоружен.")

# Класс Monster
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} побежден!")
        else:
            print(f"{self.name} получил урон, осталось {self.health} здоровья.")

# Шаг 4: Реализуем бой
def battle(fighter, monster):
    while monster.health > 0:
        fighter.attack()
        monster.take_damage(50)  # Предположим, что каждый удар наносит 50 урона

# Демонстрация
fighter = Fighter("Воин")
monster = Monster("Дракон", 100)  # У монстра 100 здоровья

# Боец выбирает оружие и атакует
fighter.change_weapon(Sword())
battle(fighter, monster)

# Боец меняет оружие и снова атакует
fighter.change_weapon(Bow())
battle(fighter, monster)

# Боец выбирает другое оружие и атакует
fighter.change_weapon(Axe())
battle(fighter, monster)
