import sys

# Error codes
EEXIST = 17 # File exists
ENOENT = 2 # No such file or directory
EINVAL = 22 # Invalid argument

# Check internal file
def check_ID(COMMAND, FS, ID):
    file = open(FS, 'r')
    lines = file.readlines()
    valid = False

    # Check if the last word of ID is '/' as it is optional
    if(ID[-1] == "/"):
        ID = ID[0:-1]

    # Check if the first or last word of ID is '/'
    if (ID[0] != "/"):
        if (COMMAND == "mkdir"):
            # ID should not exist
            if (lines.count("=" + ID + "/\n") == 1):
                error = "Invalid VSFS - mkdir: cannot create directory '" + ID + "': File exists\n"
                sys.stderr.write(error)
                exit(EEXIST)
            else:
                valid = True
        elif (COMMAND == "rmdir"):
            # ID should exist
            if (lines.count("=" + ID + "/\n") == 1):
                valid = True
            else:
                error = "Invalid VSFS - rmdir: failed to remove '" + ID + "': No such file or directory\n"
                sys.stderr.write(error)
                exit(ENOENT)
    else:
        error = "Invalid VSFS - Internal directory name should not start with '/': '" + ID + "'\n"
        sys.stderr.write(error)
        exit(EINVAL)

    file.close()
    
    return valid