for n in range(1,10):
    for x in range (2,n):
        if n % x ==0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')



        for num in  range(2,10):
            if num % 2==0:
                print("found a number", num)
                continue
                print("found a number",num)

