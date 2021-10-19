import os

from pathlib import Path

# Check internal file
def check_IF(COMMAND, FS, IF):
    if (not os.path.isabs(FS)):
        FS = Path(FS).absolute()
        
    file = open(FS, 'r')
    lines = file.readlines()
    valid = False

    if (IF[0] != "/" and IF[-1] != "/"):
        if (COMMAND == "copyin"):
            # If IF is on current directory, it should not exist
            if (IF.count("/") == 0):
                if (lines.count("@"+ IF + "\n") == 0):
                    valid = True
            else:
                # IF should not exist but sub directory of IF should exist
                print(IF[0:IF.rindex("/")])
                if (lines.count("@"+ IF + "\n") == 0 
                    and (lines.count("="+ IF[0:IF.rindex("/")] + "\n") == 1 
                    or lines.count("="+ IF[0:IF.rindex("/")] + "/\n") == 1)):
                    valid = True
        elif (COMMAND == "copyout"):
            if (lines.count("@"+ IF + "\n") == 1):
                valid = True
    file.close()

    return valid