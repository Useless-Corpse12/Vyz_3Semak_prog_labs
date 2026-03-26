import random


class Character:   

    def __init__(self, name, health, base_damage, accuracy=1.0, dodge_chance=0.0, priority=0.5):
        self.name = name
        self.class_name = self.__class__.__name__
        self.max_health = health
        self.health = health
        self.base_damage = base_damage
        self.accuracy = accuracy
        self.dodge_chance = dodge_chance
        self.priority = priority
        self.turn_count = 0

    def attack(self, target):
        self.turn_count += 1

        if random.random() > self.accuracy:
            print(f"{self.name} атакует {target.name}, но промахивается!")
            return False

        if random.random() < target.dodge_chance:
            print(f"{self.name} атакует {target.name}, но {target.name} уворачивается!")
            return False

        damage_dealt = self.calculate_damage(target)
        actual_damage = target.take_damage(self, damage_dealt)

        print(f"{self.name} атакует, нанося [{actual_damage}] урона!")
        print(f"У {target.name} [{target.health}/{target.max_health}] здоровья!")

        self.on_damage_dealt(target, actual_damage)
        self.post_attack_effects(target)

        return True

    def calculate_damage(self, target):
        return self.base_damage

    def on_damage_dealt(self, target, actual_damage):
        pass

    def post_attack_effects(self, target):
        pass

    def take_damage(self, attacker, incoming_damage):
        self.health -= incoming_damage
        self.health = max(0, self.health)
        return incoming_damage

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} ({self.class_name}, Здоровье: {self.health})"


class Knight(Character):

    def __init__(self, name):
        prefix_pool = ["Сэр", "Рыцарь", "Доблестный", "Лорд", "Благородный"]
        generated_name = f"{random.choice(prefix_pool)} {name}"
        super().__init__(name=generated_name, health=120, base_damage=15)


class Archer(Character):

    def __init__(self, name):
        suffix_pool = ["в яблочко", "белке в глаз", "орлиный глаз"]
        generated_name = f"{name} {random.choice(suffix_pool)}"
        super().__init__(name=generated_name, health=100, base_damage=25, accuracy=0.9)


class Mage(Character):

    def __init__(self, name):
        prefix_pool = ["Кудесник", "Заклинатель", "Чародей", "Сумасшедший", "Великий маг"]
        generated_name = f"{random.choice(prefix_pool)} {name}"
        super().__init__(name=generated_name, health=80, base_damage=30)

    def post_attack_effects(self, target):
        if random.randint(1, 100) <= 20:
            heal = 10
            self.health = min(self.max_health, self.health + heal)
            print(f"  {self.name} восстанавливает {heal} здоровья (маг).")

class Zombie(Character):

    def __init__(self, name):
        prefix_pool = ["Мёртвый", "Бывший", "Гниющий", "Пропавший"]
        profession_pool = ["Трактирщик", "Конюх", "Кузнец", "Мясник", "Шериф", "Монах", "Король", "Плотник", "Пастух",
                           "Священник", "Торговец"]
        generated_name = f"{random.choice(prefix_pool)} {random.choice(profession_pool)} {name}"
        super().__init__(name=generated_name, health=150, base_damage=10)

    def post_attack_effects(self, target):
        heal = 5
        self.health = min(self.max_health, self.health + heal)
        print(f"  {self.name} восстанавливает {heal} здоровья (зомби).")


class Samurai(Character):

    def __init__(self, name):
        suffix_pool = ["острый клинок", "воин цветущей сакуры", "ронин из хатидзё"]
        generated_name = f"{name}-{random.choice(suffix_pool)}"
        super().__init__(name=generated_name, health=110, base_damage=35)

    def calculate_damage(self, target):
        base_dmg = self.base_damage
        if random.randint(1, 100) <= 15:
            base_dmg *= 2
            print(f"  {self.name} наносит критический удар! (Самурай)")
        return base_dmg


class Dwarf(Character):

    def __init__(self, name):
        suffix_pool = ["крепкий кулак", "камнебород", "из Стальгорна", "из клана Чёрного Железа",
                       "из клана Громового Молота"]
        generated_name = f"{name}-{random.choice(suffix_pool)}"
        super().__init__(name=generated_name, health=130, base_damage=18)

    def take_damage(self, attacker, incoming_damage):
        final_damage = max(0, incoming_damage - 5)
        print(f"  {self.name} (Дварф) игнорирует 5 урона. Фактический урон: {final_damage}.")
        self.health -= final_damage
        self.health = max(0, self.health)
        return final_damage


class Elf(Character):

    def __init__(self, name):
        if len(name) < 3:
            generated_name = name
        else:
            generated_name = f"{name[-1].upper()}'{name[:-3]}{name[-2]}{name[-3]}"
        super().__init__(name=generated_name, health=90, base_damage=22, dodge_chance=0.25)


class Druid(Character):

    def __init__(self, name):
        prefix_pool = ["Друид", "Лесной", "Хранитель Природы", "Шепот Деревьев", "Смотритель Леса", "Певец Ветра"]
        generated_name = f"{random.choice(prefix_pool)} {name}"
        super().__init__(name=generated_name, health=100, base_damage=12)

    def post_attack_effects(self, target):
        heal = 8
        self.health = min(self.max_health, self.health + heal)
        print(f"  {self.name} восстанавливает {heal} здоровья (друид).")

    def take_damage(self, attacker, incoming_damage):
        self.health -= incoming_damage
        self.health = max(0, self.health)
        heal_amount = 8
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"  {self.name} восстанавливает {heal_amount} здоровья (друид).")
        return incoming_damage


class Paladin(Character):

    def __init__(self, name):
        suffix_pool = ["Света", "Правды", "Клятвы", "Веры", "Справедливости", "Веры и Правды"]
        generated_name = f"{name} - паладин {random.choice(suffix_pool)}"
        super().__init__(name=generated_name, health=140, base_damage=16)

    def take_damage(self, attacker, incoming_damage):
        if self.turn_count > 0 and self.turn_count % 3 == 0:
            final_damage = max(0, incoming_damage - 10)
            print(f"  {self.name} (Паладин) блокирует 10 урона. Фактический урон: {final_damage}.")
        else:
            final_damage = incoming_damage
        self.health -= final_damage
        self.health = max(0, self.health)
        return final_damage


class Necromancer(Character):

    def __init__(self, name):
        prefix_pool = ["Повелитель Мертвых", "Повелитель Теней", "Повелитель Костей", "Повелитель Забвения"]
        suffix_pool = ["Мрачный", "Тёмный", "Гнусный", "Безумный", "Терзающий"]
        generated_name = f"{random.choice(prefix_pool)} {name} {random.choice(suffix_pool)}"
        super().__init__(name=generated_name, health=95, base_damage=18)
        self.skeleton_damage_bonus = 0

    def calculate_damage(self, target):
        total_damage = self.base_damage + self.skeleton_damage_bonus
        self.skeleton_damage_bonus += 5
        print(f"  {self.name} призывает скелета. Урон в следующей атаке: {total_damage}.")
        return total_damage


class Rogue(Character):

    def __init__(self, name):
        suffix_pool = ["Гуд", "тихий шёпот", "острый клинок", "Форточник", "лёгкая рука", "хозяин теней"]
        generated_name = f"{name} {random.choice(suffix_pool)}"
        super().__init__(name=generated_name, health=105, base_damage=28)

    def calculate_damage(self, target):
        base_dmg = self.base_damage
        if random.randint(1, 100) <= 30:
            base_dmg = int(base_dmg * 1.5)
            print(f"  {self.name} наносит критический удар! (Разбойник)")
        return base_dmg


class Goblin(Character):

    def __init__(self, name):
        suffix_pool = ["Кусака", "Из Норы", "Мелкий", "Копытогрыз", "Шумелка", "Коготь"]
        generated_name = f"{name} {random.choice(suffix_pool)}"
        super().__init__(name=generated_name, health=80, base_damage=20)

    def attack(self, target):
        super().attack(target)
        if random.randint(1, 100) <= 20:
            print(f"  {self.name} атакует дважды подряд!")
            super().attack(target)


class Centaur(Character):

    def __init__(self, name):
        name_pool = ["Мустанг", "Блэк", "Ворон", "Уголёк", "Ангус", "Морион", "Оникс", "Каштан", "Браун", "Шоко",
                     "Бруно", "Кашмир", "Портер", "Мокко", "Капучино", "Бордо", "Махагон"]
        generated_name = f"{random.choice(name_pool)}"
        super().__init__(name=generated_name, health=125, base_damage=17, priority=1.7)


class Vampire(Character):

    def __init__(self, name):
        prefix_pool = ["Граф", "Вампир", "Повелитель"]
        suffix_pool = ["Крови", "Ночи", "Тьмы", "Клыка", "Теней"]
        generated_name = f"{random.choice(prefix_pool)} {random.choice(suffix_pool)} {name}"
        super().__init__(name=generated_name, health=115, base_damage=19)

    def on_damage_dealt(self, target, actual_damage):
        stolen_health = int(actual_damage * 0.5)
        self.health = min(self.max_health, self.health + stolen_health)
        print(f"  {self.name} восстанавливает {stolen_health} здоровья (вампиризм).")


class Demon(Character):

    def __init__(self, name):
        prefix_pool = ["Устрашающий", "Пылающий", "Порабощающий", "Ужасающий", "Жаждущий"]
        generated_name = f"{random.choice(prefix_pool)} {name[::-1].capitalize()}"
        super().__init__(name=generated_name, health=160, base_damage=22)

    def calculate_damage(self, target):
        base_dmg = self.base_damage
        if random.randint(1, 100) <= 40:
            base_dmg += 5
            print(f"  {self.name} зажигает! Следующий удар будет больнее! (Демон)")
        return base_dmg


class ShitCarrier(Character):

    def __init__(self, name):
        prefix_pool = ["Стена", "Камень", "Скала", "Оплот", "Бастион", "Таран"]
        generated_name = f"{random.choice(prefix_pool)} {name}"
        super().__init__(name=generated_name, health=200, base_damage=10)

    def take_damage(self, attacker, incoming_damage):
        if self.turn_count > 0 and self.turn_count % 4 == 0:
            reflected_damage = int(incoming_damage * 0.5)
            attacker.health = max(0, attacker.health - reflected_damage)
            final_damage = max(0, incoming_damage - reflected_damage)
            print(f"  {self.name} (Щитоносец) отражает {reflected_damage} урона атакующему {attacker.name}.")
            print(f"  Фактический урон по {self.name}: {final_damage}.")
        else:
            final_damage = incoming_damage
        self.health -= final_damage
        self.health = max(0, self.health)
        return final_damage


class Monk(Character):

    def __init__(self, name):
        prefix_pool = ["Спокойный", "Текущий ручей", "Крепкая скала", "Молчаливый", "Путь", "Тишина"]
        generated_name = f"{random.choice(prefix_pool)} {name}"
        super().__init__(name=generated_name, health=100, base_damage=24)

    def post_attack_effects(self, target):
        if random.randint(1, 100) <= 20:
            target.health = max(0, target.health - self.base_damage)
            print(f"  Контратака! {self.name} наносит {self.base_damage} урона.")


class Orc(Character):

    def __init__(self, name):
        replace_pool = ["Д", "Г", "Т", "К"]
        suffix_pool = ["тог", "дор", "доз", "гог", "зар", "мог"]
        threat_pool = ["Гром", "Ярость", "Смерть", "Кровь", "Разрушение"]
        new_name = f"{random.choice(replace_pool)}{name[1:]}{random.choice(suffix_pool)} {random.choice(threat_pool)}"
        generated_name = new_name
        super().__init__(name=generated_name, health=135, base_damage=26)
        self.rage_active = False

    def calculate_damage(self, target):
        base_dmg = self.base_damage
        if self.rage_active:
            base_dmg = int(base_dmg * 1.5)
        return base_dmg

    def take_damage(self, attacker, incoming_damage):
        if not self.rage_active and self.health > incoming_damage and (self.health - incoming_damage) <= (
                self.max_health / 2):
            self.rage_active = True
            print(f"  {self.name} (Орк) впадает в ярость!")
        self.health -= incoming_damage
        self.health = max(0, self.health)
        return incoming_damage


class Ghost(Character):

    def __init__(self, name):
        prefix_pool = ["Неупокоенная Душа", "Злой Дух", "Беспокойный дух", "Забвенный", "Страдающий", "Тоскующий", "Неупокоившийся"]
        generated_name = f"{random.choice(prefix_pool)} {name}"
        super().__init__(name=generated_name, health=70, base_damage=15)

    def take_damage(self, attacker, incoming_damage):
        if self.turn_count > 0 and self.turn_count % 3 == 0:
            print(f"  {self.name} (Призрак) неуязвим! Урон не получен.")
            return 0
        else:
            self.health -= incoming_damage
            self.health = max(0, self.health)
            return incoming_damage


class Inquisitor(Character):

    def __init__(self, name):
        suffix_pool = ["Света", "Еретиков", "Правосудия", "Огня", "Очищения"]
        generated_name = f"{name} - инквизитор {random.choice(suffix_pool)}"
        super().__init__(name=generated_name, health=110, base_damage=16)

    def calculate_damage(self, target):
        base_dmg = self.base_damage
        if target.class_name == "Mage":
            base_dmg += 8
            print(f"  {self.name} сжигает мангу! (+8 урона)")
        return base_dmg


class CyborgWarrior(Character):

    def __init__(self, name):
        hex_code = ''.join([format(ord(c), 'x') for c in name])
        generated_name = f"CYB-{hex_code}"
        super().__init__(name=generated_name, health=120, base_damage=18)
        self.is_recharging = False
        self.next_attack_buffed = False

    def attack(self, target):
        if self.is_recharging:
            print(f"  {self.name} пропускает ход, перезаряжается.")
            self.is_recharging = False
            self.turn_count += 1
            return True
        else:
            if random.randint(1, 100) <= 10:
                print(f"  {self.name} решает пропустить ход для перезарядки.")
                self.is_recharging = True
                self.next_attack_buffed = True
                self.turn_count += 1
                return True
            else:
                return super().attack(target)

    def calculate_damage(self, target):
        base_dmg = self.base_damage
        if self.next_attack_buffed:
            base_dmg = int(base_dmg * 1.5)
            self.next_attack_buffed = False
            print(f"  {self.name} наносит усиленную атаку! (Кибер-воин)")
        return base_dmg


class Alchemist(Character):

    def __init__(self, name):
        suffix_pool = ["Варщик", "Хайзенберг", "Пинкман", "Шалтай-болтай", "Менделеев"]
        generated_name = f"{name} {random.choice(suffix_pool)}"
        super().__init__(name=generated_name, health=95, base_damage=14)

    def calculate_damage(self, target):
        return random.randint(5, 25)


class Berserker(Character):

    def __init__(self, name):
        suffix_pool = ["Ярости", "Кровавый", "Без Страха", "Бешеный", "Воин", "Ревущий"]
        generated_name = f"{name} {random.choice(suffix_pool)}"
        super().__init__(name=generated_name, health=130, base_damage=30)

    def post_attack_effects(self, target):
        self_loss = 5
        self.health = max(0, self.health - self_loss)
        print(f"  {self.name} теряет {self_loss} здоровья от ярости (берсерк).")


class Templar(Character):

    def __init__(self, name):
        suffix_pool = ["Святого Гроба", "Молитвы", "Правосудия", "Святого Огня", "Веры"]
        generated_name = f"{name} - храмовник {random.choice(suffix_pool)}"
        super().__init__(name=generated_name, health=150, base_damage=13)
        self.prayer_cooldown = 4

    def post_attack_effects(self, target):
        if self.turn_count > 0 and self.turn_count % self.prayer_cooldown == 0:
            heal = 15
            self.health = min(self.max_health, self.health + heal)
            print(f"  {self.name} молится и восстанавливает {heal} здоровья.")


class Sniper(Character):

    def __init__(self, name):
        prefix_pool = ["Снайпер", "Меткий", "Тихий", "Верный выстрел", "Призрачный", "Тень",
                       "Косание смерти"]
        generated_name = f"{random.choice(prefix_pool)} {name}"
        super().__init__(name=generated_name, health=90, base_damage=40, accuracy=0.8)


def battle(char1, char2):
    print(f"Битва начинается между {char1} и {char2}!\n")
    total_priority = char1.priority + char2.priority
    rand_val = random.random() * total_priority

    if rand_val < char1.priority:
        attacker, defender = char1, char2
    else:
        attacker, defender = char2, char1

    while char1.is_alive() and char2.is_alive():
        total_priority = attacker.priority + defender.priority
        rand_val = random.random() * total_priority
        print()
        if rand_val < attacker.priority:
            pass
        else:
            attacker, defender = defender, attacker

        attacker.attack(defender)
        if not defender.is_alive():
            print(f"\n{defender.name} отправляется в нокаут!")
            break
        attacker, defender = defender, attacker


def tournament():
    print("ДОБРО ПОЖАЛОВАТЬ НА КРОВАВУЮ АРЕНУ СМЕРТИ!")
    print("ДАВНО МЫ НЕ УСТРАИВАЛИ ЭПИЧНЫХ СРАЖЕНИЙ!")
    print("СЕГОДНЯ И ТОЛЬКО СЕГОДНЯ ПРОХОДИТ ТУРНИР СРЕДИ НАШИХ ПРОШЛЫХ ФИНАЛИСТОВ!")
    print("БОЙ НА СМЕРТЬ!")
    print("ВСТРЕЧАЙТЕ НАШИХ УЧАСТНИКОВ -")

    pool_of_names = ["Николай", "Степан", "Иван", "Артём", "Павел", "Никита", "Григорий", "Александр", "Максим",
                     "Станислав", "Арман", "Святослав","Евгений","Магомед",]
    all_classes = [
        Knight, Archer, Mage, Zombie, Samurai, Dwarf, Elf, Druid, Paladin, Necromancer,
        Rogue, Goblin, Centaur, Vampire, Demon, ShitCarrier, Monk, Orc, Ghost,
        Inquisitor, CyborgWarrior, Alchemist, Berserker, Templar, Sniper
    ]

    gladiators = []
    for i in range(8):
        random_name = random.choice(pool_of_names)
        random_class = random.choice(all_classes)
        character = random_class(random_name)
        gladiators.append(character)
        print(f"  {character.name} ({character.class_name})")

    print("\nДА НАЧНЁТСЯ БИТВА!\n")

    current_round = gladiators

    round_number = 1
    while len(current_round) > 1:
        print(f"--- Раунд {round_number} ---")
        next_round = []

        random.shuffle(current_round)
        for i in range(0, len(current_round), 2):
            print()
            fighter1 = current_round[i]
            fighter2 = current_round[i+1]
            print("\n" + "=" * 50 + "\n")
            print(f"\nБой между {fighter1} и {fighter2}!")
            print("\n" + "=" * 50 + "\n")
            battle(fighter1, fighter2)

            if fighter1.is_alive():
                winner = fighter1
            else:
                winner = fighter2
            print("\n" + "=" * 50 + "\n")
            print(f"Победитель: {winner.name}!")
            print("\n" + "=" * 50 + "\n")
            next_round.append(winner)
            print(f"Похоже {winner.name} - немного потрёпан! Дадим отдышаться, хотя... Перед смертью не надышишься!")
            winner.health = min(winner.max_health, winner.health + int(winner.max_health * 0.25))
            print(f"  {winner.name} восстанавливает {int(winner.max_health * 0.25)} здоровья после боя.")

        current_round = next_round
        round_number += 1
        print("\n" + "="*50 + "\n")

    final_winner = current_round[0]
    print(f"ТУРНИР ОКОНЧЕН! ПОБЕДИТЕЛЬ: {final_winner.name} ({final_winner.class_name})!")


tournament()