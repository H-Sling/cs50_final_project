#The below code is a POC for triggering the sorting code from a GUI button

# import the python GUI libary as tk for easier typing in the future. 
import tkinter as tk
#import the POC to run it in this code also
import poc
# handling my image
from PIL import ImageTk, Image


# Create the window 
window = tk.Tk()

# display an image at the top of the screen (POC)
# open the image file and resize so that it is about the size of a logo
logo = Image.open("C:\\Users\\Harry\\Projects\\CS50_Final_Project\\cs50_final_project\\quizy_logo.tiff")
logo = logo.resize((100, 100), Image.ANTIALIAS)

# add the logo to a label TO DO - add this label to a frame that is the width of the GUI
logo_img = ImageTk.PhotoImage(logo)
label1 = tk.Label(image=logo_img)
label1.image = logo_img
label1.place(x=0, y=0)

#create a label and add the label to the window using the pack fucniton
greeting = tk.Label(
    text = "Press the Button to sort your folders",
    foreground="black",
    background="white"
    )
greeting.pack()
# need to install pillows libary to handle the logo
# logo - tk.Label()

# Triggers the sort code from the POC file. 
def handle_click():
    poc.main()

#add a button
button = tk.Button(
    text="Sort!",
    width=10,
    height=1,
    bg="#D4D0C8",
    fg="black", 
    borderwidth=5,
    relief=tk.RAISED, 
    command=handle_click
)
button.pack()

# necersary to get the window to display from VScode - not an issue if usign Python IDLE
window.mainloop()