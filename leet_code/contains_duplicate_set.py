def contains_duplicate(nums: list):
    count_set = set()
    for i in nums:
        if i in count_set:
            return True
        count_set.add(i)
    return False


print(contains_duplicate([1, 2, 3, 4, 5, 6, 3]))
print(contains_duplicate([1, 2, 3, 4, 5, 6, 677, 223, 44]))
