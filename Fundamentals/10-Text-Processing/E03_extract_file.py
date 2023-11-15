# Write a program that reads the path to a file and subtracts the file name and its extension.

path_file = input().split('\\')

file = path_file[-1].split('.')
file_name = file[0]
file_extension = file[1]

print(f"""File name: {file_name}
File extension: {file_extension}
""")
