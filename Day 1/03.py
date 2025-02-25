# second largest numbers
def sec_larg(num):
    return sorted(set(num))[-2]
lst = [-800 ,2,8,7,60]
print(sec_larg(lst))