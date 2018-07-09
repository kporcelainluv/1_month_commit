# my own
def modify_list(l):
    count = 0
    while True:
        if count >= len(l):
            break
        if l[count] % 2 != 0:
            del l[count]
        else:
            l[count] = l[count] // 2
            count += 1



lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)

# try to do it via filter
# getting the same link to array !!!!
#
# lst = [1, 2, 3, 4, 5, 6]
# lst[:] = [1,2,3]
# print(lst)
# just freakin copy it!

def modify_list(l):
    l[:] = filter(lambda x: x % 2 == 0, l)
    l[:] = map(lambda x: x // 2, l)
