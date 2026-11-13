nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
for i in nums:
    for j in i:
        if i + j == target:
            len(nums[i][j])
