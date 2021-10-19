# Check internal file
def check_ID(FS, ID):
    file = open(FS, 'r')
    lines = file.readlines()
    valid = False

    # Check if the first or last word of ID is '/'
    if (ID[0] != "/" and ID[-1] != "/"):
        # If ID is on current directory, it should not exist
        if (ID.count("/") == 0):
            if (lines.count("="+ ID + "/\n") == 0):
                valid = True
        else:
            # ID should not exist but sub directory of ID should exist
            if (lines.count("="+ ID + "\n") == 0 
                and (lines.count("="+ ID[0:ID.rindex("/")] + "\n") == 1
                # Check the directories on current directory which has '/' at the end 
                or lines.count("="+ ID[0:ID.rindex("/")] + "/\n") == 1)):
                valid = True
    file.close()
    
    return valid