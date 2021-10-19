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
            valid = True
            # ID should not exist
            if (lines.count("=" + ID + "/\n") == 1):
                valid = False
        elif (COMMAND == "rmdir"):
            # ID should exist
            if (lines.count("=" + ID + "/\n") == 1):
                valid = True

    file.close()
    
    return valid