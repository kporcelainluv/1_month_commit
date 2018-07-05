# my personal
# def function_of(input):
#     list_of = []
#     list_of_nums = list(range(input-(input-1), input+1))
#     for x in list_of_nums:
#         for j in range(x):
#             list_of.append(str(x))
#             if len(list_of) == len(list_of_nums):
#                 return " ".join(list_of)
# print(function_of(int(input())))

# yanis help

# list_length = int(input())
# input_list = list(range(list_length-(list_length-1), list_length+1))
#
# def solution(length, i, acc):
#     if len(acc) >= length:
#         return (map(str, acc[:length]))
#     else:
#         return solution(length, i+1, acc+(i*[i]))
#
# print(*solution(list_length, 1, []))
#

# my second try

list_length = int(input())
input_list = list(range(list_length-(list_length-1), list_length+1))

def solution(list_length, i, acc, i_amount):
    if len(acc) >= list_length:
        return acc
    else:
        if i_amount == i:
            return solution(list_length, i+1, acc, 0)
        else:
            return solution(list_length, i, acc+[i], i_amount+1)

print(solution(list_length, 1, [], 0))

# what I have learned

# list = list(range(1, 5))


