# Copy the external file, EF, into the FS as internal file named IF
def copyin(FS, EF, IF):
    EF_file = open(EF, 'r')
    IF_file = open(FS, 'a+')

    # Move cursor to the start to check last location of cursor is starting at the end of new line
    IF_file.seek(0)
    IF_lines = IF_file.readlines()
    if(IF_lines[-1][-1].isspace() is False):
        IF_file.write("\n")

    #Write @IF
    IF_file.write("@" + IF + "\n")
    EF_lines = EF_file.readlines()
    
    # Copy the content of EF into the IF
    for line in EF_lines:
        IF_file.write(" " + line)    
    
    EF_file.close()
    IF_file.close()