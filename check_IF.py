import sys

from rm import *

# Error codes
EEXIST = 17 # File exists
ENOENT = 2 # No such file or directory
EINVAL = 22 # Invalid argument

# Check internal file
def check_IF(COMMAND, FS, IF):
    file = open(FS, 'r')
    lines = file.readlines()
    valid = False

    # Check if the first or last word of IF is '/'
    if (IF[0] != "/" and IF[-1] != "/"):
        if (COMMAND == "copyin"):
            valid = True
            # IF already exists, then remove the original file
            if (lines.count("@" + IF + "\n") == 1):
                rm(FS, IF)
        elif (COMMAND == "copyout" or COMMAND == "rm"):
            # IF should exist 
            if (lines.count("@" + IF + "\n") == 1):
                valid = True
            else:
                error = "Invalid VSFS - No such file for directory: '" + IF + "'\n"
                sys.stderr.write(error)
                exit(ENOENT)
    else:
        error = "Invalid VSFS - Internal file name should not start with '/' and not end with '/': '" + IF + "'\n"
        sys.stderr.write(error)
        exit(EINVAL)
    file.close()

    return valid