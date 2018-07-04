# my original
input = list(map(int, input().split()))
my_set = set()
for i in input:
    if input.count(i) >= 2:
        my_set.add(i)
print(*my_set)

# the one that I liked

input = list(map(int, input().split()))
print(*(i for i in set(input) if input.count(i) > 1))
