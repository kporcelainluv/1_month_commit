from collections import Counter
with open("dataset_3363_2.txt") as fp:
    text = fp.read().strip("\n").lower()
    text = text.split()

most_common = sorted(Counter(text).most_common(1))
print(most_common[0][0], most_common[0][1])
