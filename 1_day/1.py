# my personal solving

string = input()
return_string = ""
number = ""
for i in string:
    if i.isdigit():
        number += i
    if i.isalpha():
        if number is "":
            number = 1
        return_string += int(number) * i
        number = ""
print(return_string)
