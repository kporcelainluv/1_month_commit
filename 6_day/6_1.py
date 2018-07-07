with open("dataset_3363_2.txt") as fp:
    text = fp.read().strip().split()
russian_middle = 0
math_middle = 0
physics_middle = 0
for student in text:
    name, math, physics, russian = student.split(";")
    print((int(math) + int(physics) + int(russian))/3)
    russian_middle += int(russian)
    math_middle += int(math)
    physics_middle += int(physics)
print(math_middle/len(text), physics_middle/len(text), russian_middle/len(text))
