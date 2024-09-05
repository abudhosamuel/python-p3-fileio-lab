

def write_file(file_name, file_content):
    # Add .txt extension to the file_name
    full_file_name = f"{file_name}.txt"
    # Open the file in write mode and write the content
    with open(full_file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # Add .txt extension to the file_name
    full_file_name = f"{file_name}.txt"
    # Open the file in append mode and add the content directly
    with open(full_file_name, 'a') as file:
        file.write(append_content)


def read_file(file_name):
    # Add .txt extension to the file_name
    full_file_name = f"{file_name}.txt"
    # Open the file in read mode and return its content
    with open(full_file_name, 'r') as file:
        return file.read()
