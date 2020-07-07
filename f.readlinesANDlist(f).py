with open('Testing File.txt') as f:

    print(list(f))
    f.close()
with open('Testing File.txt') as f:

    print(f.readlines())
    f.close()