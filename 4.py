def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Number of lines: {sum(1 for line in file)}")
    except FileNotFoundError:
        print("File not found!")

filename = input("Enter the file name: ")
count_lines(filename)