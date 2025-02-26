def Rectangle_pyramid(n):
    for i in range(1, n+1):
        for j in  range(n-i):
            print("*",end =" ")
        for k in range(1, 3+i):
            print("*", end =" ")
        print()

print(Rectangle_pyramid(2))