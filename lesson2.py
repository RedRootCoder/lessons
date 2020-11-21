# Програмка ищет длину окружности:
import math
radius = float(input('Введите радиус: ')) # ввод данных от пользователя
diameter = radius * 2
c = math.pi * (diameter) # нахождение окружности 
round_var = round(c, 3) # округляем найденную окружность до 3 знаков после запятой
print(round_var)