import re

# Copy the external file, EF, into the FS as internal file named IF
def copyin(FS, EF, IF):
    EF_file = open(EF, 'r')
    IF_file = open(FS, 'a+')

    # Move cursor to the start to check last location of cursor is starting at the end of new line
    IF_file.seek(0)
    IF_lines = IF_file.readlines()
    if(IF_lines[-1][-1].isspace() is False):
        IF_file.write("\n")

    # Check subdirectories already exist
    index = [m.start() for m in re.finditer(r"/", IF)]
    for i in range(len(index)):
        if (IF_lines.count("=" + IF[0:index[i]] + "/\n") == 0):
            IF_file.write("=" + IF[0:index[i]] + "/\n")
        
    # Write @IF
    IF_file.write("@" + IF + "\n")

    EF_lines = EF_file.readlines()

    # Check the length of content of EF
    if (len(EF_lines) > 255):
        EF_lines = EF_lines[0:255]
    
    # Copy the content of EF into the IF with empty space at the start
    for line in EF_lines:
        IF_file.write(" " + line)    
    
    EF_file.close()
    IF_file.close()