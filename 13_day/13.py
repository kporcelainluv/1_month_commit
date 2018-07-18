#link https://stepik.org/lesson/21299/step/4?adaptive=true&unit=5100
# first solving
#
# string = input()
# string += " "
# letter = string[0]
# counter = 0
# string_return = ""
# for i in range(len(string)):
#     if string[i] == letter:
#         counter += 1
#     else:
#         string_return += (str(counter)+letter if counter != 1 else letter)
#         counter = 1
#         letter = string[i]
# print(string_return)

# second solving

string = input()
string += " "

#returns [(3, "a"), (1, 'b'), (4, 'c') etc]
def split_encode_series(string):
    string_return = []
    letter = string[0]
    counter = 0
    for i in range(len(string)):
        if string[i] == letter:
            counter += 1
        else:
            string_return.append((counter, letter))
            counter = 1
            letter = string[i]
    return string_return

# returns 3ab4c2CaB
def encode_series(series):
    new_str = ""
    for i in series:
        new_str += (str(i[0])+i[1] if i[0] != 1 else i[1])
    return new_str

#returns total value
def rle_encode(string):
    series = split_encode_series(string)
    return encode_series(series)

print(rle_encode(string))
