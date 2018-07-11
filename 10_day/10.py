input_list, input_number = list(map(int, input().split())), int(input())
if input_number not in input_list:
    print("None")
else:
    for index, number in enumerate(input_list):
        if number == input_number:
            print(index, end=" ")
