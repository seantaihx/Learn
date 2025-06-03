'''
Write a function read_file(filename) that opens and reads a file.
	•	Use try-except to handle FileNotFoundError.
	•	If the file doesn’t exist, return "File not found".
'''

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

print(read_file("existing_file.txt"))  # Prints file content
print(read_file("missing_file.txt"))   # File not found

'''SAMPLE OUTPUT
@seantaihx ➜ .../Practice/Python/Practices/5Function (main) $ python Q4ans.py
File not found
File not found
@seantaihx ➜ .../Practice/Python/Practices/5Function (main) $ 
'''