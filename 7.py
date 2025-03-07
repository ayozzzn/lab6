import shutil

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found!")

src = input("Enter source filename: ")
dest = input("Enter destination filename: ")
copy_file(src, dest)