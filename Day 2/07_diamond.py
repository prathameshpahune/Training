
def diamond_pyramid(n):
    for i in range(1, n+1):
        for j in  range(1, n-i+1):
            print("",end ="")
        for k in range(1, 2*i):
            print("*", end ="")
        print()

    for i in range(n-2,-1,-1):
        for j in  range(n-i):
            print(" ",end =" ")
        for k in range(1, 2*i):
            print("*", end =" ")
        print()


print(diamond_pyramid(5))