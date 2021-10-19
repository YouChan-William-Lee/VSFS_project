import re

# Create empty internal directory ID in FS
def mkdir(FS, ID):
    file = open(FS, 'a+')

    # Check if the last word of ID is '/'
    if (ID[-1] == "/"):
        ID = ID[0:-1]

    # Move cursor to the start to check last location of cursor is starting at the end of new line
    file.seek(0)
    lines = file.readlines()
    if (lines[-1][-1].isspace() is False):
        file.write("\n")

    # Check subdirectories already exist
    index = [m.start() for m in re.finditer(r"/", ID)]
    for i in range(len(index)):
        if (lines.count("=" + ID[0:index[i]] + "/\n") == 0):
            file.write("=" + ID[0:index[i]] + "/\n")
    
    # Make ID
    file.write("=" + ID + "/\n")

    file.close()
