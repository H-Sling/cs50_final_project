# libary for file manipulation
from shutil import move
# to read the file extention
from pathlib import Path
# libary to read from the directory
import os


# To Do - Need to make it so that the source dir can be user selected

def Sort(src, dst_txt):
    files = []
    for entry in os.scandir(path=src):
        files.append(entry.path)

    # Define the destination folders
    txt_dst = dst_txt
    img_dst = "C:\\Users\\Harry\\Projects\\CS50_Final_Project\\test_dst_img"
    pdf_dst = "C:\\Users\\Harry\\Projects\\CS50_Final_Project\\test_dst_pdf"

    for item in files:    
        # Get the file extention for sorting
        file_extention = Path(item).suffix

        # sort based on the file extention
        if file_extention == ".txt":
            move(item, txt_dst)
        elif file_extention == ".JPG":
            move(item, img_dst)
        elif file_extention == ".pdf":
            move(item, pdf_dst)
        else:
            break
    
    return True


