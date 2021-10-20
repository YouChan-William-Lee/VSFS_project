import os

# List the contents of FS in 'ls -lR' format 
def list(FS, dir, is_last_dir):
    file_info = "file_info"
    command = "ls -l " + FS + " > " + file_info
    os.system(command)
    # Save the information of FS
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
        # Print total size
        print(".:\ntotal", total_size)
        for index, line in enumerate(lines):
            # Check files
            # Ex) a file on current directory is @note1
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
                # Print file information    
                print("-" + attribute, "%3s"%1, owner, group, file_size, month, day, time, os.getcwd() + "/" + line[1:], end = '')
            # Check directories
            # Ex) a directory on current directory is =dir1/
            elif (line[0] == "=" and line.count("/") == 1 and line.find("/") + 1 == line.find("\n")):
                # Print directory information
                print("d" + attribute, "%3s"%check_number_of_subdir(FS, line[1:-2]), owner, group, 0, month, day, time, os.getcwd() + "/" + line[1:-2])
    else:
        print("./" + dir + ":\ntotal", total_size)
        for index, line in enumerate(lines):
            # Check files
            # Ex) a file on a sub directory is @dir1/note when dir is dir1
            if (line[0] == "@" and line.count("/") == dir.count("/") + 1 and line.find(dir) == 1):
                # Check the size how many lines in the file
                file_size = 0
                file_index = index
                while(True):
                    if (file_index < len(lines) - 1 and lines[file_index + 1][0].isspace()):
                        file_size += 1
                        file_index += 1
                    else:
                        break
                # Print file information  
                print("-" + attribute, "%3s"%1, owner, group, file_size, month, day, time, os.getcwd() + "/" + line[1:], end = '')
            # Check directories
            # Ex) a directory on a sub directory is =dir1/dir2/ when dir is dir1
            elif (line[0] == "=" and line.count("/") == dir.count("/") + 2 and line.find(dir) == 1):
                # Print directory inforamtion
                print("d" + attribute, "%3s"%check_number_of_subdir(FS, line[1:-2]), owner, group, 0, month, day, time, os.getcwd() + "/" + line[1:-2])
    
    # If dir is last one, then don't print new line
    if (is_last_dir is False):
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
        # Check directories
        if (line[0] == "="):
            # 1 condition Ex) line is dir1/dir2/ and dir is dir1, then dir1 has dir2 as a sub directory 
            # 2 condition Ex) line is dir1/dir2/ and dir is dir2, then it is not sub directory
            if (line.count("/") == dir.count("/") + 2 and line.find(dir) == 1):
                total_number_of_subdir += 1

    file.close()
    return total_number_of_subdir

# Check total subdirectories recursively 
def check_subdir(FS):
    dirs = ['current']
    file = open(FS, 'r')
    lines = file.readlines()
    for line in lines:
        # Check directories
        if (line[0] == "="):
            dirs.append(line[1:-2])

    file.close()
    return sorted(dirs)