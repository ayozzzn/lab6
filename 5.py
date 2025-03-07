def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

data = ["Hello", "World", "Python", "File Handling"]
filename = "output.txt"
write_list_to_file(filename, data)
print("List written to file successfully.")