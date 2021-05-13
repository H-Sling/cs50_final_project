# libary for file manipulation
from shutil import move
# to read the file extention
from pathlib import Path
# libary to read from the directory
import os


# To Do - Need to make it so that the source dir can be user selected

def Sort(src, dst1, fle1):
    files = []
    for entry in os.scandir(path=src):
        files.append(entry.path)

    # Define the destination folders
    dst_1 = dst1

    for item in files:    
        # Get the file extention for sorting
        file_extention = Path(item).suffix

        # sort based on the file extention
        if file_extention == fle1:
            move(item, dst_1)
    
    return True


