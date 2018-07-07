with open("dataset_3363_2.txt") as fp:
    text = fp.read().strip()
string = ""
count = 0
return_string = ""
for i in range(len(text)):
    if text[i].isalpha() and i>0:
        char, number = string[0], string[1:]
        return_string += char * int(number)
        string = text[i]
    else:
        string += text[i]
        if i == len(text)-1:
            char, number = string[0], string[1:]
            return_string += char * int(number)

print(return_string)
