
l = [("Alice", 25, "New York"), ("Bob", 17, "Los Angeles"), ("Charlie", 30, "Chicago")]


lst = {t[0]:t[1] for t in l if t[1] > 20}

print(lst) 


