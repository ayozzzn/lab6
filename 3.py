import os

def check_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print("Path does not exists.")

path = input("Enter the path: ")
check_path()