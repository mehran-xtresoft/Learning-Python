with open('Testing File Read.txt') as f:
    print(f.readline())
    print(f.readline())

    read_data = f.read()
    print(read_data)
    print(f.closed)
