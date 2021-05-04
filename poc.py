# Below POC moves a file from one directory on the storage to another based on the defined file extentions. 

# libary for file manipulation (particualry copy)
from shutil import move
# to read the file extention
from pathlib import Path
# libary to read from the directory
import os


#adding in a line to test git!
print("hello, world") 

def main():
    files = []
    for entry in os.scandir(path='C:\\Users\\Harry\\Projects\\CS50_Final_Project\\test_source'):
        files.append(entry.path)

    for item in files:
        if not run_copy(item):
            print("error")
            break
       # print("Sucessfully Completed")


def run_copy(item):
    # define the destination folders and the source file
    txt_dst = "C:\\Users\\Harry\\Projects\\CS50_Final_Project\\test_dst_txt"
    img_dst = "C:\\Users\\Harry\\Projects\\CS50_Final_Project\\test_dst_img"
    pdf_dst = "C:\\Users\\Harry\\Projects\\CS50_Final_Project\\test_dst_pdf"
    src = item
    
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
        return False
    return True

# main()
# the above is commented out to stop it from running when imported into the GUI program!