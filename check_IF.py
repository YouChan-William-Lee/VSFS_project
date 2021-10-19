# Check internal file
def check_IF(COMMAND, FS, IF):
    file = open(FS, 'r')
    lines = file.readlines()
    valid = False

    # Check if the first or last word of IF is '/'
    if (IF[0] != "/" and IF[-1] != "/"):
        if (COMMAND == "copyin"):
            # If IF is on current directory, it should not exist
            if (IF.count("/") == 0):
                if (lines.count("@" + IF + "\n") == 0):
                    valid = True
            else:
                # IF should not exist but sub directory of IF should exist
                if (lines.count("@" + IF + "\n") == 0 and lines.count("=" + IF[0:IF.rindex("/")] + "/\n") == 1):
                    valid = True
        elif (COMMAND == "copyout" or COMMAND == "rm"):
            # IF should exist 
            if (lines.count("@" + IF + "\n") == 1):
                valid = True
    file.close()

    return valid