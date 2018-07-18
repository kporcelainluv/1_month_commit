def h():
    print("- 3")
    print("- 12")
    print("3 - end")

def f():
    print("- 2")
    g(h)
    print("2 - end")

def g(a):
    print("- 1 - ",a)
    a()
    print("1 - end")

print("\nMODULE")
g(f)

# 2 сделать работающую рекурсию на редьюсе
from functools import reduce
def closest_mod_5(x):
    return (reduce(lambda x: x % 5 == 0, closest_mod_5(x+1)))


print(closest_mod_5(10))
