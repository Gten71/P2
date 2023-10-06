import math

class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __del__(self):
        print("Объект удален.")

    def multiply(self, scalar):
        self.real *= scalar
        self.imag *= scalar

    def calculate_argument(self):
        argument_radians = math.atan2(self.imag, self.real)
        argument_degrees = math.degrees(argument_radians)
        return argument_degrees

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Создание объекта с заданными значениями
complex_num = ComplexNumber(3, 4)

# Вывод информации о комплексном числе
print("Комплексное число:", complex_num)

# Умножение на введенное число (например, 2)
scalar = float(input("Введите число для умножения: "))
complex_num.multiply(scalar)
print("Результат умножения:", complex_num)

# Вычисление аргумента в градусах
argument_degrees = complex_num.calculate_argument()
print("Аргумент в градусах:", argument_degrees)
