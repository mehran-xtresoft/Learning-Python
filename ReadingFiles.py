with open('Testing File.txt') as f:
    print(f.readline())
    print(f.readline())

    read_data = f.read()
    print(read_data)
    print(f.closed)
