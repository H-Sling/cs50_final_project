# TODO - allows destination files to be user selected via GUI
# TODO - improve UI for version 1
# TODO - V2 - give use a list of all found file types and ask where to send each


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

# open the image file and resize so that it is about the size of a logo
logo = Image.open("C:\\Users\\Harry\\Projects\\CS50_Final_Project\\cs50_final_project\\quizy_logo.tiff")
logo = logo.resize((100, 100), Image.ANTIALIAS)

# add the logo to a label
logo_img = ImageTk.PhotoImage(logo)
label1 = tk.Label(image=logo_img)
label1.image = logo_img
label1.pack()

# A welcome message at the top of the app screen
greeting = tk.Label(
    text = "Welcome to the tidy app!",
    foreground="black",
    background="white"
    )
greeting.pack()

# Get the user input for the source file when the button is pressed
def get_src():
    src = filedialog.askdirectory()
    source.insert(0, src)

#button for the user to choose the source file to sort. 
browse_src = tk.Button(
    text="Select Folder to tidy-up",
    width=20,
    height=2,
    bg="#D4D0C8",
    fg="black", 
    borderwidth=5,
    relief=tk.RAISED, 
    command=get_src
)
browse_src.pack()

# Create a label to store the Source path in; TODO - make the label responsive to the text
source = tk.Entry(width=75)
source.pack()

# Get the user input for the source file when the button is pressed
def get_dst1():
    dst = filedialog.askdirectory()
    dst1.insert(0, dst)

#button for the user to choose the source file to sort. 
browse_dst1 = tk.Button(
    text="Select folder to send .txt files to",
    width=20,
    height=2,
    bg="#D4D0C8",
    fg="black", 
    borderwidth=5,
    relief=tk.RAISED, 
    command=get_dst1
)
browse_dst1.pack()

# Create a label to store the Source path in; TODO - make the label responsive to the text
dst1 = tk.Entry(width=75)
dst1.pack()

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
    command=handle_click
)
sort.pack()

# necersary to get the window to display from VScode - not an issue if usign Python IDLE
window.mainloop()