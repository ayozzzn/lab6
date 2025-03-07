import os

def check_access(path):
    print(f"Exists: {os.path.esists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writeable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

path = input("Enter the path: ")
check_access(path)