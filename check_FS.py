import os
import sys

# Error codes
ENOEXEC = 8 # Exec format error

# Check file system
def check_FS(FS):
    valid = False
    try:
        # Check if FS is existent
        os.path.isfile(FS)
        file = open(FS, 'r')
        valid = True

        # Check the first line of FS is 'NOTES V1.0\n'
        if (valid and file.readline() != "NOTES V1.0\n"):
            error = "Invalid VSFS - invalid file system: '" + FS + "'\n"
            sys.stderr.write(error)
            exit(ENOEXEC)
            
        file.close()
    # Catch err
    except IOError as err:
        error = "Invalid VSFS - " + str(err)[10:] + "\n"
        sys.stderr.write(error)
        exit(err.errno)
    
    return valid