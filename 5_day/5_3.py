# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.

dict_of = {}
list_of = list(int(input())for i in range(int(input())))
for i in list_of:
    if i not in dict_of:
        dict_of[i] = f(i)
    print(dict_of[i])
