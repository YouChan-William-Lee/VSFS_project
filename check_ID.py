import os

from pathlib import Path

# Check internal file
def check_ID(FS, ID):
    if (not os.path.isabs(FS)):
        FS = Path(FS).absolute()

    file = open(FS, 'r')
    lines = file.readlines()
    valid = False
    subdir = ID

    if (ID[0] != "/" and ID[-1] != "/"):
        # If ID is on current directory, it should not exist
        if (ID.count("/") == 0):
            if (lines.count("="+ ID + "/\n") == 0):
                valid = True
        else:
            # ID should not exist but sub directory of ID should exist
            if (lines.count("="+ ID + "\n") == 0 
                and (lines.count("="+ ID[0:ID.rindex("/")] + "\n") == 1 
                or lines.count("="+ ID[0:ID.rindex("/")] + "/\n") == 1)):
                valid = True
    file.close()
    
    return valid