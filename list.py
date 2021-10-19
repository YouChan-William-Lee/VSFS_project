import os

# List the contents of FS in 'ls -lR' format 
def list(FS, dir):
    file_info = "file_info"
    command = "ls -l " + FS + " > " + file_info
    os.system(command)
    ls_command_result = open(file_info, 'r').read().split()
    os.remove(file_info)

    attribute = (ls_command_result[0])[1:]
    owner = ls_command_result[2]
    group = ls_command_result[3]
    month = ls_command_result[5]
    day = ls_command_result[6]
    time = ls_command_result[7]

    # Check the total size of each directory
    total_size = check_total_size(FS, dir)

    file = open(FS, 'r')
    lines = file.readlines()
    if (dir == "current"):
        print(".:")
        print("total", total_size)
        for index, line in enumerate(lines):
            # Check files
            if (line[0] == "@" and line.count("/") == 0):
                # Check the size how many lines in the file
                file_size = 0
                file_index = index
                while(True):
                    if (file_index < len(lines) - 1 and lines[file_index + 1][0].isspace()):
                        file_size += 1
                        file_index += 1
                    else:
                        break
                print("-" + attribute, "%3s"%1, owner, group, file_size, month, day, time, os.getcwd() + "/" + line[1:], end = '')
            # Check directories
            elif (line[0] == "=" and line.count("/") == 1 and line.find("/") + 1 == line.find("\n")):
                print("d" + attribute, "%3s"%check_number_of_subdir(FS, line[1:-2]), owner, group, 0, month, day, time, os.getcwd() + "/" + line[1:-2])
    else:
        print("./" + dir + ":")
        print("total", total_size)
        for index, line in enumerate(lines):
            # Check files
            if (line[0] == "@" and line.count("/") == dir.count("/") + 1 and line.find(dir) == 1):
                # Check the size how many lines in the file
                file_size = 0
                file_index = index
                while(True):
                    if (lines[file_index + 1][0].isspace()):
                        file_size += 1
                        file_index += 1
                    else:
                        break
                print("-" + attribute, "%3s"%1, owner, group, file_size, month, day, time, os.getcwd() + "/" + line[1:], end = '')
            # Check directories
            elif (line[0] == "=" and line.count("/") == dir.count("/") + 1 and line.find(dir) == 1 and line.find("/") + 1 != line.find("\n")):
                print("d" + attribute, "%3s"%check_number_of_subdir(FS, line[1:-1]), owner, group, 0, month, day, time, os.getcwd() + "/" + line[1:-1])

    print("")
    file.close()

# Check the total size of current directory
def check_total_size(FS, dir):
    total_size = 0
    file = open(FS, 'r')
    lines = file.readlines()
    if (dir == "current"):
        for index, line in enumerate(lines):
            if (line[0] == "@" and line.count("/") == 0):
                # Check the size how many lines in the file
                file_index = index
                while(True):
                    if (file_index < len(lines) - 1 and lines[file_index + 1][0].isspace()):
                        total_size += 1
                        file_index += 1
                    else:
                        break
    else:
        for index, line in enumerate(lines):
                if (line[0] == "@" and line.count("/") == dir.count("/") + 1 and line.find(dir) == 1):
                    # Check the size how many lines in the file
                    file_index = index
                    while(True):
                        if (file_index < len(lines) - 1 and lines[file_index + 1][0].isspace()):
                            total_size += 1
                            file_index += 1
                        else:
                            break
    file.close()
    return total_size

# Check total number of subdirectories of current directory
def check_number_of_subdir(FS, dir):
    total_number_of_subdir = 0
    file = open(FS, 'r')
    lines = file.readlines()
    for line in lines:
        if (line[0] == "="):
            if (line.count("/") == dir.count("/") + 1 and line.find(dir) == 1 and line.rindex("/") + 1 != line.rindex("\n")):
                total_number_of_subdir += 1

    file.close()
    return total_number_of_subdir

# Check total subdirectories recursively 
def check_subdir(FS):
    dirs = ['current']
    file = open(FS, 'r')
    lines = file.readlines()
    for line in lines:
        if (line[0] == "="):
            # Check number of directory on current directory
            if (line.count("/") == 1 and line.rindex("/") + 1 == line.rindex("\n")):
                dirs.append(line[1:-2])
            # Check number of directory when more than 2    
            elif (line.count("/") >= 1 and line.rindex("/") + 1 != line.rindex("\n")):
                dirs.append(line[1:-1])

    file.close()
    return sorted(dirs)