from functools import reduce
list_of = []
while True:
    list_of.append(int(input()))
    if reduce((lambda x, y: x+y), list_of) == 0:
        print(reduce((lambda x, y: x + y), (x**2 for x in list_of)))
        break
