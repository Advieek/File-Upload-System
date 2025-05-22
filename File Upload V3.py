import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

FOLDER_1 = "/Users/advieek/Desktop/Test 1"
FOLDER_2 = "/Users/advieek/Desktop/Test 2"
FOLDER_3 = "/Users/advieek/Desktop/Test 3"

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

    original_name = os.path.basename(src_path)
    print(f"Selected file: {original_name}")
    new_name = input(f"Enter a new name for the file (or press Enter to keep '{original_name}'): ").strip()
    if new_name == "":
        new_name = original_name
    else:
        if not os.path.splitext(new_name)[1]:
            new_name += os.path.splitext(original_name)[1]

    dest_path = os.path.join(dest_folder, new_name)

    if os.path.exists(dest_path):
        confirm = input(f"A file named '{new_name}' already exists in the destination. Overwrite? (y/n): ").strip().lower()
        if confirm != "y":
            print("Operation cancelled.")
            return

    try:
        shutil.copy(src_path, dest_path)
        print(f"File has been copied to: {dest_path}")
        messagebox.showinfo("Success", f"File copied to:\n{dest_path}")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    upload_file_to_selected_folder()
