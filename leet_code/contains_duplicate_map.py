def contains_duplicate(nums: list):
    count_num = {}
    for i in range(len(nums)):
        count_num[nums[i]] = 1 + count_num.get(nums[i], 0)
    for c in count_num:
        if count_num[c] > 1:
            return True
    return False


print(
    contains_duplicate([1, 2, 3, 4, 5, 6, 3, 5, 2, 677, 223, 677, 44, 5, 4, 45, 4, 5])
)
print(contains_duplicate([1, 2, 3, 4, 5, 6, 677, 223, 44]))
