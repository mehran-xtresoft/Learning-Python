with open('Testing File.txt', 'rb+',) as f:
    print(f.write(b'This line is added through write command.\n'))
    f.seek(5)
    print(f.read(4))
    f.seek(-10, 2)
    print(f.read(7))
