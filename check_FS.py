import os
import sys

# Check file system
def check_FS(FS):
    valid = False
    if(FS.count("/") == 0):
        try:
            os.path.isfile("./" + FS)
            file = open("./" + FS, 'r')
            valid = True
            if (valid and file.readline() != "NOTES V1.0\n"):
                valid = False
            file.close()
        except IOError as err:
            sys.stderr.write(str(err) + "\n")
            exit(err.errno)
    else:
        try:
            os.path.isfile(FS)
            file = open(FS, 'r')
            valid = True
            if (valid and file.readline() != "NOTES V1.0\n"):
                valid = False
            file.close()
        except IOError as err:
            sys.stderr.write(str(err) + "\n")
            exit(err.errno)

    return valid