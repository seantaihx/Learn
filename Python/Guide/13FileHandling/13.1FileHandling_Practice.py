# 13.0 File Handling Practice
# Covers: open, read, write, append, create, check, delete (file/folder), modes

import os

print("=== 1. Open a File and Write with 'w' mode ===")
with open("demo.txt", "w") as f:
    f.write("This is the first line.\n")
    f.write("This is the second line.\n")
print("Written with 'w' mode: content overwritten if file existed.\n")

print("=== 2. Append to the File with 'a' mode ===")
with open("demo.txt", "a") as f:
    f.write("This is the third line (appended).\n")
print("Appended to 'demo.txt'\n")

print("=== 3. Read the Whole File ===")
with open("demo.txt", "r") as f:
    content = f.read()
    print("File content:\n" + content)

print("=== 4. Read File Line by Line ===")
with open("demo.txt", "r") as f:
    print("Reading line by line using for loop:")
    for line in f:
        print(line.strip())  # strip to remove newline

print("=== 5. Read Specific Characters ===")
with open("demo.txt", "r") as f:
    partial = f.read(10)
    print("First 10 characters:", partial)

print("\n=== 6. Create a File with 'x' mode ===")
try:
    with open("new_created_file.txt", "x") as f:
        f.write("This file was created using 'x' mode.")
    print("File 'new_created_file.txt' created successfully.")
except FileExistsError:
    print("File already exists. 'x' mode cannot overwrite.")

print("\n=== 7. Check if a File Exists ===")
if os.path.exists("demo.txt"):
    print("'demo.txt' exists.")
else:
    print("'demo.txt' does not exist.")

print("\n=== 8. Delete a File ===")
if os.path.exists("new_created_file.txt"):
    os.remove("new_created_file.txt")
    print("Deleted 'new_created_file.txt'.")
else:
    print("'new_created_file.txt' does not exist.")

print("\n=== 9. Create and Delete a Folder ===")
# Create folder only if it doesn't exist
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("Folder 'test_folder' created.")

# Try to delete (only works if empty)
try:
    os.rmdir("test_folder")
    print("Folder 'test_folder' deleted (must be empty).")
except OSError:
    print("Folder 'test_folder' is not empty, cannot delete.")

print("\n=== Done! ===")
