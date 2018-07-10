arr_of_directions = list(input().split() for i in range(int(input())))
dictionary = {"север": 0, "юг": 0, "запад": 0, "восток": 0}
for line in arr_of_directions:
    dictionary[line[0]] = int(line[1])
y = abs(dictionary["север"] - dictionary["юг"])
x = abs(dictionary["запад"] - dictionary["восток"])


if dictionary["запад"] > dictionary["восток"]:
    x = x * (-1)
if dictionary["юг"] > dictionary["север"]:
    y = y * (-1)
print(x, y)
