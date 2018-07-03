# what others did and me trying to learng smth new

# 1. value = (var or 1)
string = input()
return_string = ""
number = ""
for i in string:
    if i.isdigit():
        number += i
    if i.isalpha():
        return_string += int(number or 1) * i
        number = ""
print(return_string)
