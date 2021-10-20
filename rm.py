# Remove internal file IF from FS
def rm(FS, IF):

    file = open(FS, 'r+')
    lines = file.readlines()
    newlines = ""
    # To check how many lines need to be deleted
    count = 0

    for index, line in enumerate(lines):
        # Check where IF is and put them in newlines to overwrite
        if (line[1:-1] == IF and count == 0):
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