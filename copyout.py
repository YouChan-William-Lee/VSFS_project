# Copy the internal file IF within FS to external file EF
def copyout(FS, IF, EF):
    
    IF_file = open(FS, 'r')

    if (EF.count("/") == 0):
        EF_file = open("./" + EF, 'w')
        IF_lines = IF_file.readlines()
        for index, line in enumerate(IF_lines):
            file_index = index
            if(line[1:-1] == IF):
                while(True):
                    if (IF_lines[file_index + 1][0].isspace()):
                        EF_file.write(IF_lines[file_index + 1][1:])
                        file_index += 1
                    else:
                        break
    else:
        EF_file = open(EF, 'w')
        IF_lines = IF_file.readlines()
        for index, line in enumerate(IF_lines):
            file_index = index
            if(line[1:-1] == IF):
                while(True):
                    if (IF_lines[file_index + 1][0].isspace()):
                        EF_file.write(IF_lines[file_index + 1][1:])
                        file_index += 1
                    else:
                        break