from time import sleep
from modules.reader import FileReader


reader = FileReader()

inp_user = input("Enter full path to the file:\n> ")

if inp_user == 'q':
    quit()

# Reading the user input
reader.read(inp_user)
content = reader.get_content()
print(f"File: {reader.get_filename()}\nContent:\n{content.rstrip()}")

# Printing each line of the file
print("\nEach line of content:")
lines = reader.get_lines()
for line in lines:
    index = lines.index(line)
    print(f"{index}:{line.rstrip()}")


print("\nWorking with file's contents:")

reader.read('files/one-million.txt')
lines = reader.get_lines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"\nDigits of pi_string: {len(pi_string.replace('3.', ''))}")
print(f"Showing only 52 digits:\n{pi_string[:54]}")

birthday = input("\n\nEnter your birthday in format ddmmyy:\n> ")
pi = reader.get_string()

if birthday in pi:
    print("Your birthday appears in firt million digits of Pi!")
else:
    print("Your birthday does not appears in first million digits of Pi.")
sleep(2)

# "WITH" closes the file after read methods.
with open('files/learning_python.txt', encoding='UTF-8') as file_object:
    # Reading the entire file and printing.
    print(file_object.read())

with open('files/learning_python.txt', encoding='UTF-8') as file_object:
    # Storing each line of file in a list.
    lines = file_object.readlines()
    string = ''

    # Then, print each element of the list.
    for line in lines:
        print(line.rstrip())

    # Concatenate each line to a string and print
    for line in lines:
        string += line

    print(string)

# Using replace method
with open('files/learning_python.txt', encoding='UTF-8') as fo:
    lines = fo.readlines()

lines_c = list(line.replace('python', 'C').rstrip() for line in lines)

# Printing each line:
for line in lines_c:
    print(line)
