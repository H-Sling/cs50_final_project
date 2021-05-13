# TODO - Make a dropdown list autopopulate based on the file extentions found in source (alternativly provide the user with a list of 
#        file types)
# TODO - make it so that any unsorted file types simply are left in the root folder (maybe a warning?)
# TODO - improve UI - add delete button to remove a line


# import the python GUI libary as tk for easier typing in the future. Import filedialog to use native file explorer 
import tkinter as tk
from tkinter import filedialog
#import the POC file (sort fucntion) to run it in this code also
import sorter
# Import pillows in order to handle the logo
from PIL import ImageTk, Image
# to read the file extention
from pathlib import Path
# libary to read from the directory
import os


# Global Variables
dst_count = 0

# Create the window on the users screen
window = tk.Tk()
window.geometry("500x500")
window.title("Tidy App")

#create the frames for the desired layout
frame_header = tk.Frame(master = window, pady=2, padx=2)
frame_src = tk.Frame(master = window, pady=2, padx=2)
frame_file_types = tk.Frame(master = window, pady=2, padx=2)
frame_dst = tk.Frame(master = window, pady=2, padx=2)
frame_button = tk.Frame(master = window, pady=2, padx=2)
frame_header.grid(row=0, column=0)
frame_src.grid(row=1, column=0)
frame_file_types.grid(row=2, column=0)
frame_dst.grid(row=3, column=0)
frame_button.grid(row=4, column=0)

# open the image file and resize so that it is about the size of a logo
logo = Image.open("C:\\Users\\Harry\\Projects\\CS50_Final_Project\\cs50_final_project\\quizy_logo.tiff")
logo = logo.resize((100, 100), Image.ANTIALIAS)
logo_img = ImageTk.PhotoImage(logo)
label1 = tk.Label(image=logo_img, master = frame_header)
label1.image = logo_img
label1.grid(row=0, column=0)

# A welcome message at the top of the app screen
greeting = tk.Label(
    master=frame_header,
    text = "Welcome to the tidy app!",
    font=("Helvetica", 22),
    )
greeting.grid(row=0, column=1)

# layout for the source section
frame_src_inst = tk.Frame(frame_src)
frame_src_entry = tk.Frame(frame_src)
frame_src_inst.pack()
frame_src_entry.pack()

# Get the user input for the source file when the button is pressed
def get_src():

    # Clear any previous entries
    source.delete(0, "end")
    ext.delete(0, "end")

    # Populate the Source box
    src = filedialog.askdirectory()
    source.insert(0, src)

    # Identify the files in the source folder
    files = []
    for entry in os.scandir(path=src):
        files.append(entry.path)    

    # Identify and sotre the file extentions
    file_ext = []
    for item in files:    
        # Ensure no duplications in what is presented to the user
        if Path(item).suffix not in file_ext:
            file_ext.append(Path(item).suffix)
    
    # Display the file extentions in the label
    ext.insert(0, file_ext)

# Instructional Label
src_label = tk.Label(text="Select a folder to tidy!", master=frame_src_inst)
src_label.pack()

#button for the user to choose the source file to sort. 
browse_src = tk.Button(
    master=frame_src_entry, 
    text="Browse",
    width=7,
    height=1,
    bg="#D4D0C8",
    fg="black", 
    borderwidth=5,
    relief=tk.RAISED, 
    command=get_src
)
browse_src.grid(row=0, column=1)

# Create a label to store the Source path in
source = tk.Entry(master=frame_src_entry, width=55)
source.grid(row=0, column=0)

# Code and label to return a list of file types
ext_label = tk.Label(frame_file_types, text="File Types in Source Folder")
ext_label.pack()
ext = tk.Entry(frame_file_types)
ext.pack()


# Define the lists of elements for the dst lines
dst = []
file_type = []

def new_dst():
    #referance global variables
    global dst_count
    global dst
    global file_type
    i = dst_count

    # Get the user input for the source file when the button is pressed
    def get_dst():
        dst_loc = filedialog.askdirectory()
        dst[i].insert(0, dst_loc)


    # layout for the source section
    frame_dst_inst = tk.Frame(frame_dst)
    frame_dst_entry = tk.Frame(frame_dst)
    frame_dst_inst.pack()
    frame_dst_entry.pack()

    # Instructional Label
    dst_label = tk.Label(frame_dst_inst, text="Select the file type and destination folder!")
    dst_label.pack()

    # Placeholder for file type dropdown
    typ = tk.Entry(frame_dst_entry, width=5)
    file_type.append(typ)
    file_type[i].grid(row=0, column=0)

    #button for the user to choose the source file to sort. 
    browse_dst = tk.Button(
        master=frame_dst_entry,
        text="Browse",
        width=7,
        height=1,
        bg="#D4D0C8",
        fg="black", 
        borderwidth=5,
        relief=tk.RAISED, 
        command=get_dst
    )
    browse_dst.grid(row=0, column=2)

    # Create a label to store the Source path in; TODO - make the label responsive to the text
    destination = tk.Entry(frame_dst_entry, width=50)
    dst.append(destination)
    dst[i].grid(row=0, column=1)

    # Keep count of the number of dsts added - NOT WORKING!
    dst_count += 1

new_dst()

# New Dst button - allows the user to add a line in the visual code
sort = tk.Button(
    master=frame_button,
    text="+ file type",
    width=7,
    height=1,
    bg="#D4D0C8",
    fg="black", 
    borderwidth=5,
    relief=tk.RAISED, 
    command=new_dst  
)
sort.pack()
# On click - trigger the sort fucntion
# NOTE: Does this fucntion need to be triggered mutliple times and only handle one file type and destination at a time?
def handle_click():
    for i in range(dst_count):
        sorter.Sort(source.get(), dst[i].get(), file_type[i].get())

# Sort button 
sort = tk.Button(
    master=frame_button,
    text="Tidy",
    width=7,
    height=1,
    bg="#D4D0C8",
    fg="black", 
    borderwidth=5,
    relief=tk.RAISED, 
    command=handle_click  
)
sort.pack()

# necersary to get the window to display
window.mainloop()