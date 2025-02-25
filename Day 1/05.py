# good Pairs

def count_good_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and i < j:
                count += 1
    return count

print(count_good_pairs([1,3,2,1,1,3]))