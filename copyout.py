# Copy the internal file IF within FS to external file EF
def copyout(FS, IF, EF):
    
    IF_file = open(FS, 'r')
    EF_file = open(EF, 'w')
    IF_lines = IF_file.readlines()
    
    for index, line in enumerate(IF_lines):
        file_index = index
        # Find IF
        if(line[1:-1] == IF):
            # Find the content of the IF
            while(True):
                if (file_index < len(IF_lines) - 1 and IF_lines[file_index + 1][0].isspace()):
                    # Write the content into EF
                    EF_file.write(IF_lines[file_index + 1][1:])
                    file_index += 1
                else:
                    break