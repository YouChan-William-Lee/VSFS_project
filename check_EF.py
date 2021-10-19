import os
import sys

# Check external file 
def check_EF(COMMAND, EF):
    valid = False
    if (EF.count("/") == 0 and COMMAND == "copyin"):
        try:
            file = open("./" + EF, 'r')
            valid = os.path.isfile("./" + EF)
            file.close()
        except IOError as err:
            sys.stderr.write(str(err) + "\n")
            exit(err.errno)
    elif (EF.count("/") == 0 and COMMAND == "copyout"):
        try:
            open("./" + EF, 'x')
            valid = os.path.isfile("./" + EF)
        except IOError as err:
            sys.stderr.write(str(err) + "\n")
            exit(err.errno)
    elif (EF.count("/") != 0 and COMMAND == "copyin"):
        try:
            file = open(EF, 'r')
            valid = os.path.isfile(EF)
            file.close()
        except IOError as err:
            sys.stderr.write(str(err) + "\n")
            exit(err.errno)
    elif (EF.count("/") != 0 and COMMAND == "copyout"):
        try:
            open(EF, 'x')
            valid = os.path.isfile(EF)
        except IOError as err:
            sys.stderr.write(str(err) + "\n")
            exit(err.errno)  

    return valid