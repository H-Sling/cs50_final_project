# TODO SUnday 9th May - get dropdown of file extentions found in the root folder
    # Make a dropdown list autopopulate based on the file extentions found in source and
    # ensure that the users entry is taken into the sort fucniton. 
    # copy the existing destination frame to get the app working in POC form again
# TODO - add a "+" button to allow the user to add more rows for further file types and destinations
# TODO - make it so that any unsorted file types simply are left in the root folder (maybe a warning?)
# TODO - improve UI


# import the python GUI libary as tk for easier typing in the future. Import filedialog to use native file explorer 
import tkinter as tk
from tkinter import filedialog
#import the POC file (sort fucntion) to run it in this code also
import sorter
# Import pillows in order to handle the logo
from PIL import ImageTk, Image


# Create the window on the users screen
window = tk.Tk()
window.geometry("500x500")
window.title("Tidy App")

#create the frames for the desired layout
frame_header = tk.Frame(master = window, pady=2, padx=2)
frame_src = tk.Frame(master = window, pady=2, padx=2)
frame_inst2=tk.Frame(master=window, pady=1, padx=2)
frame_dst1 = tk.Frame(master = window, pady=2, padx=2)
frame_button = tk.Frame(master = window, pady=2, padx=2)
frame_header.grid(row=0, column=0)
frame_src.grid(row=1, column=0)
frame_dst1.grid(row=2, column=0)
frame_button.grid(row=3, column=0)

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
    src = filedialog.askdirectory()
    source.insert(0, src)

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

# Get the user input for the source file when the button is pressed
def get_dst1():
    dst = filedialog.askdirectory()
    dst1.insert(0, dst)


# layout for the source section
frame_dst1_inst = tk.Frame(frame_dst1)
frame_dst1_entry = tk.Frame(frame_dst1)
frame_dst1_inst.pack()
frame_dst1_entry.pack()

# Instructional Label
dst1_label = tk.Label(frame_dst1_inst, text="Select the file type and destination folder!")
dst1_label.pack()

# Placeholder for file type dropdown
file_type1 = tk.Entry(frame_dst1_entry, width=5)
file_type1.grid(row=0, column=0)

#button for the user to choose the source file to sort. 
browse_dst1 = tk.Button(
    master=frame_dst1_entry,
    text="Browse",
    width=7,
    height=1,
    bg="#D4D0C8",
    fg="black", 
    borderwidth=5,
    relief=tk.RAISED, 
    command=get_dst1
)
browse_dst1.grid(row=0, column=2)

# Create a label to store the Source path in; TODO - make the label responsive to the text
dst1 = tk.Entry(frame_dst1_entry, width=50)
dst1.grid(row=0, column=1)

# On click - trigger the sort fucntion
def handle_click():
    sorter.Sort(source.get(), dst1.get())

# Sort button 
sort = tk.Button(
    text="Tidy",
    width=20,
    height=2,
    bg="#D4D0C8",
    fg="black", 
    borderwidth=5,
    relief=tk.RAISED, 
    command=handle_click,
    master=frame_button
)
sort.pack()

# necersary to get the window to display from VScode - not an issue if usign Python IDLE
window.mainloop()