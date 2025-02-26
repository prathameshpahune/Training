#Generator Comprehension - Fibonacci Sequence

#The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers.     

n = 10
"""
for i in range(1,n+1):
    i = (i-1)+(i)
    print(i)
    """
a,b = 0,1

for i in range(1, n+1):
    c = a + b
    a = b
    b = c
print(b) 
