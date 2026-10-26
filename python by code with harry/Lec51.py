with open("file.text", "r") as f:
    f.seek(10)
    print(f.read(5))
    f.close
    