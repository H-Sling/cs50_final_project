# cs50_final_project
#### Video Demo:  
#### Description
The [...] app helps users to organise their cluttered folders in a user friendly and quick way. The main use of this application would be to sort neglatected download folders, however the user can chose any source folder and so any folder with mutltiple files types can be sorted. 

The application is designed to be as user friedly as possible. The app makes use of the native file explorers on the users machine to allow for easy file identification. Once a folder is selected, the applicaiton will create a new line for each file type that was found in the source folder, simplifying the process for the user, and allowing for the user to select any destination folder (or none) that they desire. 

While the python code used in this project is realtivly simple, the construction and design of the GUI was a challenge. Additionally the application was designed to handle a number of "incorrect" user cases and inform the user of their error rather than simply crash. Some of the erorr handling also posed a challenge, both to identifiy possible errors, and to handle them in an intuative way. The applicaiton was built in stages from a simply CMD line python script, to a single button on a GUI resulting finally in the finished product. This application was build in VScode and utilised GITHUB as the code repository. 

 The {...} file is the GUI code. The GUI is built using Tkinter. Tkinters filedialog function was used to access the users native file explorer in the OS. Pathlib and OS python libaries were used to handle the reading of the files in a folder and finding the file extentions. Pillows was installed in order to handle the application logo (original design curtasy of Svetlana Okladnykh). 

 The sorter.py file is the code which is behind the "..." button. This is written in python and makes use of the shutil libary to move files between folders, and the pathlib and OS liaries to read the files and find the file extentions as in the GUI file. While the main sorting code is quite simple (~10 lines) this function attempts to accomodate posisble user errors to either produce a favorable result, or display a visual error in a worse case situation to allow the user to correct their error. 

#### How to use
1. Open the appliation
2. Chose the folder to be tidied by click on "Browse" to open file exporer or manually typing the file location
3. Once you have chose your destination folder, the applicaiton will automatically create a new line for each file type which is found in the folder. Chose a destination for each file type through the "Browse" button, or by manually typeing the desitnation folder location. 
4. If you dont wish to move a certian file type from its original location - simply leave the destination blank. 
5. Once all destination folders are assigned, click on the tidy button to sort the files to the desired destinations.
