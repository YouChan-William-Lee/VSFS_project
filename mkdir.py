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
    # Ex) ID is dir1/dir2/dir3, then index of '/' is 4 and 9
    index = [m.start() for m in re.finditer(r"/", ID)]
    for i in range(len(index)):
        # Check all sub directories such as dir1 and dir1/dir2 whether they already exist
        if (lines.count("=" + ID[0:index[i]] + "/\n") == 0):
            # If the sub directory doesn't exist, then create it 
            file.write("=" + ID[0:index[i]] + "/\n")
    
    # Make ID such as dir1/dir2/dir3
    file.write("=" + ID + "/\n")
    file.close()