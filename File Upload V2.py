import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Predefined destination folders
FOLDER_1 = "File Path 1"
FOLDER_2 = "File Path 2"
FOLDER_3 = "File Path 3"

FOLDER_OPTIONS = {
    "1": FOLDER_1,
    "2": FOLDER_2,
    "3": FOLDER_3
}

def upload_file_to_selected_folder():
    print("Select destination folder:\n1 - Folder 1\n2 - Folder 2\n3 - Folder 3")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice not in FOLDER_OPTIONS:
        print("Invalid choice. Exiting.")
        return

    dest_folder = FOLDER_OPTIONS[choice]

    root = tk.Tk()
    root.withdraw()

    print("Select the source file you want to upload...")
    src_path = filedialog.askopenfilename(title="Select the source file")

    if not src_path:
        print("No source file selected. Exiting.")
        return

    try:
        filename = os.path.basename(src_path)
        dest_path = os.path.join(dest_folder, filename)
        shutil.copy(src_path, dest_path)
        print(f"File '{filename}' has been copied to: {dest_path}")
        messagebox.showinfo("Success", f"File copied to:\n{dest_path}")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    upload_file_to_selected_folder()
