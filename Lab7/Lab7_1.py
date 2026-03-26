class FixedElement:

    def __init__(self, x, y):
        self.area = x * y


class LivingRoom:

    def __init__(self, length, width):
        self.length= length
        self.width = width
        self.fixed_elements = []
        self.KoBPuKu=[]


    def add_element(self, w, h):
        self.fixed_elements.append(FixedElement(w, h))


    def carpet_area(self,carpet_width):
        area = self.length * self.width
        for i in self.fixed_elements:
            area -= i.area
        area = max(0,area)
        semi_stripe1 =area / (self.length * carpet_width)
        semi_stripe2 = area / (self.width * carpet_width)
        MB = min(semi_stripe1,semi_stripe2)
        return {
                 'FS':self.length * self.width,
                 'S': area,
                 's': int(MB)+(1 if MB != int(MB) else 0),
                 'l': self.length if semi_stripe1 < semi_stripe2 else self.width
               }


print("=== Расчет коврового покрытия ===")

length = float(input("Длина комнаты (м): "))
width = float(input("Ширина комнаты (м): "))

room = LivingRoom(length, width)

action = input("Добавить элемент (д/н)? ").lower()
while action == 'д':
    room.add_element(float(input("Ширина элемента (м): ")), float(input("Высота элемента (м): ")))
    action = input("Добавить элемент (д/н)? ").lower()

carpet_width = float(input("Ширина ковра (м): "))

options = room.carpet_area(carpet_width)

print(f"Полная площадь: {options['FS']:.2f} м²")
print(f"Полезная площадь: {options['S']:.2f} м²")
print(f"Полос нужно: {options['s']} шт")
print(f"длинна каждой полосы: {options['l']} м")