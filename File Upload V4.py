import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

FOLDER_1 = "/Users/your_username/Documents/Test 1"
FOLDER_2 = "/Users/your_username/Documents/Test 2"
FOLDER_3 = "/Users/your_username/Documents/Test 3"

FOLDER_OPTIONS = {
    "1": FOLDER_1,
    "2": FOLDER_2,
    "3": FOLDER_3
}

MAX_FILES = 5

def upload_files_to_selected_folder():
    print("Select destination folder:\n1 - Folder 1\n2 - Folder 2\n3 - Folder 3")
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice not in FOLDER_OPTIONS:
        print("Invalid choice. Exiting.")
        return

    dest_folder = FOLDER_OPTIONS[choice]

    root = tk.Tk()
    root.withdraw()

    print(f"Select up to {MAX_FILES} files you want to upload...")
    src_paths = filedialog.askopenfilenames(title=f"Select up to {MAX_FILES} files")

    if not src_paths:
        print("No files selected. Exiting.")
        return

    if len(src_paths) > MAX_FILES:
        print(f"Too many files selected ({len(src_paths)}). Limit is {MAX_FILES}. Exiting.")
        messagebox.showwarning("Too Many Files", f"Please select no more than {MAX_FILES} files.")
        return

    for src_path in src_paths:
        original_name = os.path.basename(src_path)
        print(f"\nSelected file: {original_name}")
        new_name = input(f"Enter a new name for this file (or press Enter to keep '{original_name}'): ").strip()
        if new_name == "":
            new_name = original_name
        else:
            if not os.path.splitext(new_name)[1]:
                new_name += os.path.splitext(original_name)[1]

        dest_path = os.path.join(dest_folder, new_name)

        if os.path.exists(dest_path):
            confirm = input(f"A file named '{new_name}' already exists. Overwrite? (y/n): ").strip().lower()
            if confirm != "y":
                print("Skipped.")
                continue

        try:
            shutil.copy(src_path, dest_path)
            print(f"Copied to: {dest_path}")
        except Exception as e:
            print(f"Failed to copy '{original_name}': {e}")

    messagebox.showinfo("Upload Complete", f"Finished uploading {len(src_paths)} file(s).")

if __name__ == "__main__":
    upload_files_to_selected_folder()
