import os

from pathlib import Path

# Create empty internal directory ID in FS
def mkdir(FS, ID):
    if (not os.path.isabs(FS)):
        FS = Path(FS).absolute()

    ID_file = open(FS, 'a+')

    # Move cursor to the start to check last location of cursor is starting at the end of new line
    ID_file.seek(0)
    IF_lines = ID_file.readlines()
    if(IF_lines[-1][-1].isspace() is False):
        ID_file.write("\n")

    #Write =ID
    ID_file.write("=" + ID + "\n")
    ID_file.close()