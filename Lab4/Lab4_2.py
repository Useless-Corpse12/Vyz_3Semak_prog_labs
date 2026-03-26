data_lines = []

def match_passenger(allPass, query):
    matches = []
    for name, info in allPass.items():
        if query.lower() in name.lower():
            matches.append((name, info))
    return matches

def select_passenger(matches):
    if not matches:
        print("Даже близко нет таких")
        return None
    elif len(matches) == 1:
        name, info = matches[0]
        print(f'Найден : {name}')
        print(f'Рейс: {info[0]} | Вещей: {info[1]} | Вес: {info[2]}')
        return name, info
    else:
        print("Найдено больше одного соответствия:")
        for i, (name, info) in enumerate(matches, 1):
            print(f'{i}. {name}')
        try:
            choice = int(input("Выберите подходящий вариант: ")) - 1
            if 0 <= choice < len(matches):
                name, info = matches[choice]
                print(f'Найден {name}')
                print(f'Рейс: {info[0]} | Вещей: {info[1]} | Вес: {info[2]}')
                return name, info
            else:
                print("Таких нет")
                return None
        except ValueError:
            print("Неправильно что-то ты сделал")
            return None

def search_by_flight(flight_num):
    result = []
    for name, info in ThePassenger.items():
        if info[0].upper().strip() == flight_num.upper().strip():
            result.append((name, info))
    return result


def find_FatAss_passenger():
    FatAss_name = None
    FatAss_weight = -1
    FatAss_info = None

    for name, info in ThePassenger.items():
        weight = info[2]
        if weight > FatAss_weight:
            FatAss_weight = weight
            FatAss_name = name
            FatAss_info = info

    if FatAss_name is not None:
        print(f"Пассажир с максимальным весом: {FatAss_name}")
        print(f"Рейс: {FatAss_info[0]} | Вещей: {FatAss_info[1]} | Вес: {FatAss_weight}")
        return FatAss_name, FatAss_info
    else:
        print("Нет пассажиров.")
        return None


def find_passengers_with_weight_at_least(min_weight):
    matches = []
    for name, info in ThePassenger.items():
        weight = info[2]
        if weight >= min_weight:
            matches.append((name, info))

    if not matches:
        print(f"Нет пассажиров с весом багажа не менее {min_weight} кг.")
        return None

    print(f"Найдено {len(matches)} пассажир(ов) с весом багажа не менее {min_weight} кг:")
    for name, info in matches:
        print(f"  {name} — Рейс: {info[0]} | Вещей: {info[1]} | Вес: {info[2]} кг")

    return matches

def Fatnas_Analiz(pass_dict):
    max_weight = -1
    FatAss_name = None
    FatAss_flight = None

    for name, info in pass_dict.items():
        weight = info[2]
        if weight > max_weight:
            max_weight = weight
            FatAss_name = name
            FatAss_flight = info[0]

    if FatAss_name is None:
        print("Нет данных о пассажирах.")
        return

    total_items = 0
    total_weight = 0
    count = 0

    for name, info in pass_dict.items():
        if info[0] == FatAss_flight:
            total_items += info[1]
            total_weight += info[2]
            count += 1

    print(f"Пассажир с максимальным весом багажа: {FatAss_name}")
    print(f"Вес: {max_weight} кг, рейс: {FatAss_flight}")
    print(f"\nСтатистика по рейсу {FatAss_flight}:")
    print(f"  Пассажиров: {count}")
    print(f"  Общее количество вещей: {total_items}")
    print(f"  Общий вес багажа: {total_weight}")

with open("ThePassenger.txt", encoding="utf-8") as f:
    data_lines = f.readlines()

ThePassenger = {}
for line in data_lines:
    parts = line.strip().split('|')
    name = parts[0]
    flight = parts[1]
    items = int(parts[2])
    weight = int(parts[3])
    ThePassenger[name] = [flight, items, weight]

print("Все:")
print(ThePassenger)
print("Поиск по имени")
select_passenger(match_passenger(ThePassenger,input('Enter name : ')))
print("Поиск по весу (не менее)")
find_passengers_with_weight_at_least(int(input('Enter weight number : ')))
print("Поиск по рейсу")
print(search_by_flight (input('Enter flight number : ')))
print("")
Fatnas_Analiz(ThePassenger)
