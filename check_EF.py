import os
import sys

# Check external file 
def check_EF(COMMAND, EF):
    valid = False

    # If command is 'copyin'
    if (COMMAND == "copyin"):
        try:
            # Check if EF is existent
            file = open(EF, 'r')
            valid = os.path.isfile(EF)
            file.close()
        # Catch err
        except IOError as err:
            error = "Invalid VSFS - " + str(err)[10:] + "\n"
            sys.stderr.write(error)
            exit(err.errno)
    # If commnad is 'copyout'
    elif (COMMAND == "copyout"):
        try:
            # Check if EF is existent
            open(EF, 'x')
            valid = os.path.isfile(EF)
        # Catch err
        except IOError as err:
            error = "Invalid VSFS - " + str(err)[11:] + "\n"
            sys.stderr.write(error)
            exit(err.errno)

    return valid