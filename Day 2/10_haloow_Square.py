def hollow_rectangle(r, c):

    for i in range(r):
        for j in range(c):
            if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()  

hollow_rectangle(5, 5) 
