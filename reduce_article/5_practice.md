Условие
Дано 10 целых чисел.
Вычислите их сумму.
Напишите программу, использующую наименьшее число переменных.

from functools import reduce
k = reduce(lambda x,y: x+y, list(int(input()) for _ in range(10)))
