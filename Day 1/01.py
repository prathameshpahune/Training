def closet_to_zero(num):
    return min(num,key = lambda x:abs(x))
lst= [-800, -6, 2,8,7]
print(closet_to_zero(lst))