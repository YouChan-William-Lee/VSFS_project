# Check internal file
def check_IF(COMMAND, FS, IF):
    file = open(FS, 'r')
    lines = file.readlines()
    valid = False

    # Check if the first or last word of IF is '/'
    if (IF[0] != "/" and IF[-1] != "/"):
        if (COMMAND == "copyin"):
            valid = True
            # IF should not exist
            if (lines.count("@" + IF + "\n") == 1):
                valid = False
        elif (COMMAND == "copyout" or COMMAND == "rm"):
            # IF should exist 
            if (lines.count("@" + IF + "\n") == 1):
                valid = True
    file.close()

    return valid