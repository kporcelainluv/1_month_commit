word_to_check = list(input().lower() for i in range(int(input())))
new_list = []
set_of_words = set()
for i in range(int(input())):
    register = input().split()
    for j in range(len(register)):
        if j not in word_to_check:
            set_of_words.add(word_to_check[j])
print(set_of_words)
