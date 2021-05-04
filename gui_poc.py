#The below code is a POC for triggering the sorting code from a GUI button

# import the python GUI libary as tk for easier typing in the future. 
import tkinter as tk
#import the POC to run it in this code also
import poc


# Create the window 
window = tk.Tk()
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