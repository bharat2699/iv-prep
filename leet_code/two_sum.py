def two_sum(nums: list, target: int) -> list:
    prev_nums = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_nums:
            return [prev_nums[diff], i]
        prev_nums[n] = i
    return [-1, -1]


print(two_sum(nums=[1, 2, 3, 5], target=5))
