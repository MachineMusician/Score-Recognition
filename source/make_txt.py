# make image annotations
# for square, label centered image

import os

note_name = ["Eight", "Half", "Quarter", "Sixteenth", "Whole"]
image_size = 256

path = "data_{}/data/datasets-train/Notes/".format(image_size)

for note in note_name:
    file_list = os.listdir(path + note)

    for file in file_list:
        print(file)
        f = open(path+"Label/"+file[:-4]+".txt", "w")
        f.write(str(note_name.index(note))+" 0.5 0.5 0.1875 0.1875")  # class x_center y_center width height


path = "data_{}/data/datasets-val/Notes/".format(image_size)

for note in note_name:
    file_list = os.listdir(path + note)

    for file in file_list:
        f = open(path+"Label/"+file[:-4]+".txt", "w")
        f.write(str(note_name.index(note))+" 0.5 0.5 0.1875 0.1875")