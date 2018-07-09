schifre1, schifre2, encode, decode = list(input() for i in range(4))

zip_of_shifre = list(zip(schifre1, schifre2))

def return_letter_encode(letter, resultList, idx1, idx2):
    for i in resultList:
        if i[idx1] == letter:
            return i[idx2]


for i in encode:
    print(return_letter_encode(i, zip_of_shifre, 0, 1), end="")
print()
for i in decode:
    print(return_letter_encode(i, zip_of_shifre, 1, 0), end="")
