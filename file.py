count = 0
with open("test.txt", "r") as fp:
    lines = fp.readlines()
    count = len(lines)
with open("newFile.txt", "w") as fp:
    for line in lines:
        if (count == 3):
            count -= 1
            continue
        else:
            fp.write(line)
        count-=1