"""
15_4.py open an exception instance for a nonexistent file 15_4.txt .
This program will have an exception handler that lists the file as nonexistent
and prints the contents of the file if the exists
"""
fn = 'ch15_4.txt'
try:
    with open(fn) as file_Obj:
        data = file_Obj.read()
except FileNotFoundError:
    print("can not find "+fn+" file")
else:
    print(data)
