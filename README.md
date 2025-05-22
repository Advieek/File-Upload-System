# File-Upload-System 

V1
The version 1 system of this works in a much more rudementary manner and was designer purley to test the upload system with the use of the new functions.
This simply asks for a file path for the upload which can work on various systems, and then following that asks for the file path of the item you want to move.
Accordingly, it achieves it so and so far, basic tests on my Mac have worked well enough to show that this works.

Imports:
os: For handling file paths.
shutil: To copy the file.
tkinter: For GUI file/folder selection and alerts.

upload_file_to_folder() function:
Initializes tkinter without showing a main window.
Opens a GUI dialog to let you choose the source file (using askopenfilename).
Opens a GUI dialog to choose the destination folder (using askdirectory).
Combines the destination folder path and the filename to form the full destination path.
Uses shutil.copy to copy the file to the selected folder.
Shows a pop-up message on success or error.

Running the function:
When you run the script, it immediately calls upload_file_to_folder().

What's listed above contains the imports as well as the general process for how the code runs and works, and the tasks happening in the background to achieve this



V2
The new function added to the V2 uploader is that now you are able to presave certain/definite file paths, which would then mean that rather than copying in folder paths of where you want things to be sent off to, you can simply select the corresponding folder and then paste the file path of the file

Predefined Folders
You define three destination folders at the top of the script. These are stored as variables and grouped into a dictionary that maps your input choice (1, 2, or 3) to the corresponding path.

Prompt User for Folder Choice
When you run the script, it asks you to choose a folder by entering 1, 2, or 3. If your input is not valid, the script exits.

File Selection
After choosing the folder, a file dialog window opens so you can select the file you want to upload.

File Copy
The script copies the selected file into the folder you chose earlier. It keeps the same file name.

Success or Error Message
If the file was copied successfully, a pop-up window confirms it. If an error occurs, it shows an error message instead.

What's listed above is how the code goes about running the code, the overall process is exactly the same as before, just with preloaded file paths, which improves the User Experience



V3
The V3 version improves the user experience through the prevention of duplicate files in folders, as well as allowing the user to rename the files they choose to upload which would enhance the overall organization and structure of the folder experience. This also lets me set up a version later to allow for a much more streamlined file search system, which would be good for finding and bringing back files 

Choose a Folder
The script prompts you to enter 1, 2, or 3 to choose one of the three predefined destination folders.

Select a File
A file dialog window opens. You use it to pick a single file you want to upload from your computer.

Rename Option
After selecting the file, the script asks if you want to rename it. You can press Enter to keep the original name, or type a new one. If you don’t include a file extension in the new name, it adds the original extension automatically.

Check for Existing File
Before copying, the script checks if a file with the same name already exists in the chosen folder. If it does, you're asked whether to overwrite it. If you say no, the copy of that file is cancelled.

Copy the File
If all checks pass, the script copies the file into the destination folder.

Show Result
A message box confirms that the file was copied successfully, or shows an error if something went wrong.



V4
V4 now includes support for multiple files and a customizable max file limit so that a user can only put in a certain number of files, which can prevent any big crashes from happening or huge bottlenecks with someone trying to upload high volumes of files. Currently, the limit is 5 files

