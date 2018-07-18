
from decimal import Decimal
dict_of_means = {"mile": 1609, "yard": 0.9144, "foot": 0.3048,
                 "inch": 0.0254, "km": 1000, "cm": 0.01,
                 "m": 1, "mm": 0.001}
number, unit_from, preposition, unit_to = input().split()
print('%.2e' % Decimal(float(number) * dict_of_means[unit_from] / dict_of_means[unit_to]))

