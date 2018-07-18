from functools import reduce
def closest_mod_5(x):
    return (reduce(lambda x: x % 5 == 0, closest_mod_5(x+1)))


print(closest_mod_5(10))
