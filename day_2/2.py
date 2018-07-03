# my original solving
first_range = list(range(int(input()), int(input())+1))
second_range = list(range(int(input()), int(input())+1))
print('     ', end="")
for i in range(len(second_range)):
    print(second_range[i], end="    ")
    if i == len(second_range)-1:
        print()
for i in range(len(first_range)):
    print(first_range[i], end="    ")
    for j in range(len(second_range)):
        print(first_range[i]* second_range[j], end="    ")
        if j == len(second_range)-1:
            print()

# solving of mates
a, b, c, d = (int(input()) for i in range(4))
print("", *range(c, d + 1), sep="\t")
for x in range(a, b + 1):
    print(x, *[x * y for y in range(c, d + 1)], sep='\t')
