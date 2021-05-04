# First version of the full file sorter - use should be able to select their source and destination folders via a GUI 
# Further enhancements to come will include the ability to extract all file extentions found in a folder and ask the user to specify which folder to send each to
# libary for file manipulation (particualry copy)
from shutil import move
# to read the file extention
from pathlib import Path
# libary to read from the directory
import os


# To Do - Need to make it so that the source dir can be user selected

def Sort():
    source = input("Which folder do you want to sort?")
    files = []
    for entry in os.scandir(path=source):
        files.append(entry.path)

    # Define the destination folders
    txt_dst = input("Select a folder to sort .txt files in")
    img_dst = input("Select a folder to sort .JPG files in")
    pdf_dst = input("Select a folder to sort .pdf files in")

    for src in files:    
        # Get the file extention for sorting
        file_extention = Path(src).suffix

        # sort based on the file extention
        if file_extention == ".txt":
            move(src, txt_dst)
        elif file_extention == ".JPG":
            move(src, img_dst)
        elif file_extention == ".pdf":
            move(src, pdf_dst)
        else:
            print("Error")
            return False
    
    return True

# Users can now select the source and destination folders via CMD
# Sort()


