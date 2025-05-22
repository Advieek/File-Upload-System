import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def upload_file_to_folder():
    root = tk.Tk()
    root.withdraw()

    print("Select the source file you want to upload...")
    src_path = filedialog.askopenfilename(title="Select the source file")

    if not src_path:
        print("No source file selected. Exiting.")
        return

    print("Select the destination folder where you want to upload the file...")
    dest_folder = filedialog.askdirectory(title="Select destination folder")

    if not dest_folder:
        print("No destination folder selected. Exiting.")
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
    upload_file_to_folder()
