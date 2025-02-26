"""
rn = 10
for i in range(1,rn+1):
    


# O/p: oedf
# 
# 
# 
# 
# 
# 
# 
   
r = range(10)
2 in r

r[2]
len(r)

creating a funtion that
batch 
input list, batch size


lst = [1,3,4,5,6,7,8,9,10]
batch_size = 5

for i in range(lst):
    if i <= 5:
        print(i)
"""

def process_data_in_batch(data, batch_size):
    data_size = len(data)
    for start_index in range(0,data_size, batch_size):
        end_index = min( start_index + batch_size , data_size)
        batch = data[start_index:end_index]
        print(f"processing data {start_index} and {end_index}")
        #print(batch)

data = list(range(430))
process_data_in_batch(data,50)



