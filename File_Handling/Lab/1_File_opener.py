try:
    open("file.txt")
    print("File found.")
except FileNotFoundError:
    print("File not found.")