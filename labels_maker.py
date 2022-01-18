from imutils import paths

label_mapping = {
    "airplane": 0,
    "car": 1,
    "cat": 2,
    "dog": 3,
    "elephant": 4
}

test_ims = list(paths.list_images("./test/"))
test_labels = list(map(lambda x: (x,x.split("/")[-1].split("_")[0]), test_ims))
for i in test_labels:
    if i[1] not in label_mapping.keys():
        print(i)
# test_labels_int = list(
#     map(lambda x: , test_ims)
# )

test_labels_int = []
for x in test_labels:
    test_labels_int.append(x[0].split("/")[-1] + " : " + x[1] + "\n")

with open("test_labels", "w+") as f:
    
    f.writelines(test_labels_int)