import os
import shutil

path = 'E:\Bartek\Zdjęcia\Wszystko obecnie backup'
destination = "E:\Bartek\Zdjęcia\Wszystko obecnie backup\Duplicates2"
entries = []
dup_dict = {}
endings = ["(1)", "(2)", "(3)", "(4)", "(5)", "(6)", "(7)", "(8)", "(9)"]


def looking_for_duplicates(name):
    if name in dup_dict.keys():
        dup_dict[name] += 1
    else:
        dup_dict[name] = 1


def file_type(name):
    l_file_type = []
    for char in reversed(list(name)):
        l_file_type.append(char)
        if char == '.':
            break
    forward_to_backwards = reversed(l_file_type)
    return "".join(forward_to_backwards)


with os.scandir(path) as files:
    for file in files:
        if file.is_file():
            entries.append(file.name)


for entry in entries:
    print(entry)

    type_length = len(file_type(entry))
    word_length = len(entry)

    without_file_type = entry[:word_length - type_length]

    print(without_file_type)

    if without_file_type[-3:] in endings:
        shutil.move(path + '\\' + entry, destination)


print("Done!")

