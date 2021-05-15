# import the python GUI libary as tk for easier typing in the future.
# Import StrngVar to create read only entry fields. 
# Import filedialog to use native file explorer.
# Import messagebox to display message to the user
# Import constraints 
import tkinter as tk
from tkinter import StringVar, filedialog, messagebox
from tkinter.constants import DISABLED, RIGHT, Y
# import the sorter function code
import sorter
# Import pillows in order to handle the logo
from PIL import ImageTk, Image
# Import Path and OS in order to check the folders exist and read the file extentions
from pathlib import Path
import os


# Global Variables that need to be used by various functions
dst_count = 0
file_exts =[]
dst = []
file_type = []

# Create the window on the users screen
window = tk.Tk()
window.geometry("500x500")
window.title("File Tidy")
window.iconbitmap("C:\\Users\\Harry\\Projects\\CS50_Final_Project\\cs50_final_project\\quizy.ico")

# Create the frames for the desired layout
frame_header = tk.Frame(master = window, pady=2, padx=2)
frame_src = tk.Frame(master = window, pady=2, padx=2)
frame_dst = tk.Frame(master = window, pady=2, padx=2)
frame_button = tk.Frame(master = window, pady=2, padx=2)
frame_header.pack()
frame_src.pack()
frame_dst.pack()
frame_button.pack()

# Open the image file and resize
logo = Image.open("C:\\Users\\Harry\\Projects\\CS50_Final_Project\\cs50_final_project\\quizy_logo.png")
logo = logo.resize((100, 100), Image.ANTIALIAS)
logo_img = ImageTk.PhotoImage(logo)
label1 = tk.Label(image=logo_img, master = frame_header)
label1.image = logo_img
label1.grid(row=0, column=0)

# A welcome message at the top of the app screen
greeting = tk.Label(
    master=frame_header,
    text = "Welcome to File Tidy!",
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
    # For easier use in this fucntion
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

    # Populate the file types in read only entry fields
    fletyp = StringVar()
    typ = tk.Entry(frame_dst_entry,
        textvariable=fletyp,
        state=DISABLED, 
        width=5
        )
    file_type.append(typ)
    file_type[i].grid(row=0, column=0)
    fletyp.set(file_exts[i])

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

    global file_exts
    global dst_count
    global file_exts
    global dst
    global file_type

    # Clear any previous entries and clear the dst frames & data
    source.delete(0, "end")
    dst_count = 0
    file_exts =[]
    dst = []
    file_type = []
    for widget in frame_dst.winfo_children():
        widget.pack_forget()

    # Populate the Source box
    src = filedialog.askdirectory()
    source.insert(0, src)

    # Identify the files in the source folder
    files = []
    for entry in os.scandir(path=src):
        files.append(entry.path)    

    # Identify and sotre the file extentions
    for item in files:    
        # Ensure no duplications in what is presented to the user
        if Path(item).suffix not in file_exts:
            file_exts.append(Path(item).suffix)
    
    # Filter to remove blanks from the list
    file_exts = list(filter(None, file_exts))
    
    # Give the user an error if the folder has no files.
    if not file_exts:
        messagebox.showerror("No files found at location", "There are no files in this folder!")
    
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

# Tidy button code
def handle_click():
    # Display an error message if the user has not selected a sorce folder
    if not source.get():
        messagebox.showerror("No folder selected", "Please select a folder to tidy!")
        return
    # Display an error message if the source folder cannot be located
    if not os.path.isdir(source.get()):
        messagebox.showerror("Error", "Source folder cannot be found. Please check input")
        return
    
    # Check and process the desired destination folders
    for i in range(dst_count):
        # If the destination is blank - ignore
        if not dst[i].get():
            continue
        # Display an error message if the destination folder cannot be located
        elif not os.path.isdir(dst[i].get()):
            messagebox.showerror("Error", f"Destination folder for {file_type[i].get()} file type could not be located")
            break
        # If all checks have been passed, execute the sort code.
        else:
            sorter.Sort(source.get(), dst[i].get(), file_type[i].get())
    # Inform the user that the sort completed without errors. Need to display different error if code errored out
    messagebox.showinfo("Complete", "All files have been moved to their destination folders")
    return

# Sort button 
sort = tk.Button(
    master=frame_button,
    text="Tidy!",
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