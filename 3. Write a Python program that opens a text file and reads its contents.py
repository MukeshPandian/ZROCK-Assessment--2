file_name = input("Enter the name of the text file: ")
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return "File not found."
    except IOError:
        return "Error reading the file."
print("Contents of the file ",(read_file(file_name)))
