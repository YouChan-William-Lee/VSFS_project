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
        # Check if any sub directories of ID exist, then put them in newlines to overwrite
        # Ex) line is =dir1/dir2/dir1/dir2/ and ID is dir1/dir2
        if (line[1:-1].count(ID) >= 1 and line.find(ID) == 1 and count == 0):
            # write the line needs to be deleted into newlines
            newlines += "#" + line[1:]
            file_index = index
            count += 1
            # Check next lines until meets another file or directory
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

    # Move cursor to the start
    file.seek(0)
    # Overwrite with newlines
    file.write(newlines)
    file.close()