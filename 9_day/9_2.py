dict_of_classes = {}
with open("q.txt", "r") as fp:
    list_of_students = fp.readlines()
for i in list_of_students:
    student_class, last_name, height = i.split()
    student_class = int(student_class)
    if student_class not in dict_of_classes:
        dict_of_classes[student_class] = {"height": 0, "num_of_sudents": 0}
    dict_of_classes[student_class]["num_of_sudents"] += 1
    dict_of_classes[student_class]["height"] += int(height)
for i in range(1, 12):
    if i in dict_of_classes:
        dict_of_classes[i]["height"] = dict_of_classes[i]["height"] / dict_of_classes[i]["num_of_sudents"]
    else:
        dict_of_classes[i] = {"height": "-"}


for i in sorted(dict_of_classes):
    print(i, dict_of_classes[i]["height"])
