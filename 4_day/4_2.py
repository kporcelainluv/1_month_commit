# my solving
list_of, number = list(map(int, input().split())), int(input())
kk = list(zip(range(len(list_of)), list_of))
for i in range(len(kk)):
    if number not in list_of:
        print("Отсутствует")
        break
    if kk[i][1] == number:
        print(kk[i][0], end=" ")

# wow solving I found and recreated

list_of, number = list(map(int, input().split())), int(input())
kk = list(filter(lambda x: list_of[x] == number, range(len(list_of))))
print(" ".join(map(str, kk)))
