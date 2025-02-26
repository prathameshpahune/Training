
def diamond_pyramid(n):
    for i in range(1, n+1):
        for j in  range(n-i):
            print("",end ="")
        for k in range(1, 1+i):
            print("*", end =" ")
        print()
    print(below_traingle(n))

def below_traingle(n):
    for i in range(n):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(1,i):
            print("*", end="")
    print()


print(diamond_pyramid(5))