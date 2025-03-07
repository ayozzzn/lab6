import os

def delete_file(filepath):
    if os.path.exists(filepath):
        if os.access(filepath, os.W_OK):
            os.remove(filepath)
            print("File deleted successfully.")
        else:
            print("No write access to delete the file.")
    else:
        print("File does not exist.")

filepath = input("Enter file path to delete: ")
delete_file(filepath)
