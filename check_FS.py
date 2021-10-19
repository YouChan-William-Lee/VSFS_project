import os
import sys

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
            valid = False
        file.close()
    # Catch err
    except IOError as err:
        sys.stderr.write(str(err) + "\n")
        exit(err.errno)

    return valid