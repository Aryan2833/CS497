#TwoSum LeetCode Problem Solution
nums = [2,7,11,15]
target = 9
for p1 in range(len(nums)):
    for p2 in range(p1+1,len(nums)):
        if nums[p2] == target - nums[p1]:
            print(p1,p2)
