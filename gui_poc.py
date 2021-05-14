# TODO - make it so that any unsorted file types simply are left in the root folder (maybe a warning?)
# TODO - think or some dumb user mistakes and account for them (e.g. destination does exist gives a visible error message)
# TODO - improve UI - 
        # give the widow a scroll bar if dst extend off bottom of screen
        # add delete button to remove a line
        # make it so that clicking the browse button resets the desination frames


# import the python GUI libary as tk for easier typing in the future. Import filedialog to use native file explorer 
import tkinter as tk
from tkinter import filedialog
#import the sorter function code
import sorter
# Import pillows in order to handle the logo
from PIL import ImageTk, Image
# to read the file extention
from pathlib import Path
# in order to read the files in the source folder
from os import scandir


# Global Variables
dst_count = 0
file_exts =[]
dst = []
file_type = []

# Create the window on the users screen
window = tk.Tk()
window.geometry("500x500")
window.title("Tidy App")

#create the frames for the desired layout
frame_header = tk.Frame(master = window, pady=2, padx=2)
frame_src = tk.Frame(master = window, pady=2, padx=2)
frame_dst = tk.Frame(master = window, pady=2, padx=2)
frame_button = tk.Frame(master = window, pady=2, padx=2)
frame_header.grid(row=0, column=0)
frame_src.grid(row=1, column=0)
frame_dst.grid(row=2, column=0)
frame_button.grid(row=3, column=0)

# open the image file and resize
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

# Fucntion to create the new destination line
def new_dst():
    
    #referance global variables
    global dst_count
    global dst
    global file_type
    global file_exts
    i = dst_count

    # Destination browse button action
    def get_dst():
        dst_loc = filedialog.askdirectory()
        dst[i].insert(0, dst_loc)

    # layout for the destination section
    frame_dst_inst = tk.Frame(frame_dst)
    frame_dst_entry = tk.Frame(frame_dst)
    frame_dst_inst.pack()
    frame_dst_entry.pack()

    # Instructional Label
    dst_label = tk.Label(frame_dst_inst, text="Select a destination folder for this file type!")
    dst_label.pack()

    # Populate the file types
    typ = tk.Entry(frame_dst_entry, width=5)
    file_type.append(typ)
    file_type[i].grid(row=0, column=0)
    file_type[i].insert(0, file_exts[i])

    # Destination Browse button
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

    # Create a label to store the Source path in
    destination = tk.Entry(frame_dst_entry, width=50)
    dst.append(destination)
    dst[i].grid(row=0, column=1)

    # Keep count of the number of dsts added
    dst_count += 1

# Get the user input for the source file when the button is pressed
def get_src():

    global dst_count
    global file_exts

    # Clear any previous entries
    source.delete(0, "end")

    # Populate the Source box
    src = filedialog.askdirectory()
    source.insert(0, src)

    # Identify the files in the source folder
    files = []
    for entry in scandir(path=src):
        files.append(entry.path)    

    # Identify and sotre the file extentions
    for item in files:    
        # Ensure no duplications in what is presented to the user
        if Path(item).suffix not in file_exts:
            file_exts.append(Path(item).suffix)
    
    # Display the file extentions in the label
    for file_ext in file_exts:
        new_dst()

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