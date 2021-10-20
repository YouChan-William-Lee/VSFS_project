# Check internal file
def defrag(FS):
    file = open(FS, 'r')
    lines = file.readlines()
    count = 0
    newlines = ""

    # Find lines starting with '#'
    for line in lines:
        if (line[0] == "#"):
            count += 1
        # If count is not 0, then it means the lines are added into newlines, so don't add them again
        elif (count == 0):
            newlines += line

        # If count is not 0, then skip the line
        if (count != 0):
            count -= 1
    file.close()

    file = open(FS, 'w')
    file.seek(0)
    # Overwrite with newlines
    file.write(newlines)

    file.close()