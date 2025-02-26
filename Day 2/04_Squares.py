def Square_pyramid(n):
    for i in range(1, n+1):
        for j in  range(n-i):
            print("*",end =" ")
        for k in range(1, 1+i):
            print("*", end =" ")
        print()

print(Square_pyramid(5))
