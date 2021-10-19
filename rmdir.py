import re

# Create empty internal directory ID in FS
def rmdir(FS, ID):
    file = open(FS, 'r+')
    lines = file.readlines()
    newlines = ""
    # To check how many lines need to be deleted
    count = 0

    # Check if the last word of ID is '/'
    if (ID[-1] == "/"):
        ID = ID[0:-1]

    for index, line in enumerate(lines):
        # Check where any sub directories of ID are and put them in newlines to overwrite
        if (line[1:-1].count(ID) >= 1 and line.find(ID) == 1 and count == 0):
            newlines += "#" + line[1:]
            file_index = index
            count += 1
            while(True):
                if (file_index < len(lines) - 1 and lines[file_index + 1][0].isspace()):
                    newlines += "#" + lines[file_index + 1][1:]
                    file_index += 1
                    count += 1
                else:
                    break
        # If count is not 0, then it means the lines are added into newlines, so don't add them again
        elif (count == 0):
            newlines += line

        # If count is not 0, then skip the line
        if (count != 0):
            count -= 1

    file.seek(0)
    # Overwrite with newlines
    file.write(newlines)
    file.close()