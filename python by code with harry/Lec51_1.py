with open("file.text","r") as f:
    data = f.read(10)
    current_position = f.tell()
    f.seek(current_position)
    