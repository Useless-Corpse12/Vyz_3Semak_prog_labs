class Volume:
    def __init__(self, liters):
        self.liters = float(liters)

    def __call__(self, value):
        self.liters = float(value)

    def __add__(self, other):
        if isinstance(other, Volume):
            return Volume(self.liters + other.liters)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Volume):
            return Volume(self.liters - other.liters)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Volume(self.liters * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("помилуй господь твою грешную душу")
            return Volume(self.liters / other)
        return NotImplemented

    def convert(self, unit):
        if unit == 'мл':
            result = self.liters * 1000
        elif unit == 'Гал':
            result = self.liters / 3.78541
        elif unit == 'м^3':
            result = self.liters / 1000
        else:
            raise ValueError(f"?? че за : {unit}")

        return f"{self.liters} Л = {result} {unit}"

    def __str__(self):
        return f"{self.liters} Л"


BlueRabbit = Volume(0.473)
Druidmeister = Volume(0.5)
print(Druidmeister.convert("Гал"))
shaker= (BlueRabbit+Druidmeister) #взрыв
print(shaker.convert('мл'))

