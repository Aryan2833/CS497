#Second Problem Solution for Assignment 1
def searchingRange(nums, target):
    def binarySearch(nums, target, left_bound):
        left_index, right_index = 0, len(nums) - 1
        result = -1

        while left_index <= right_index:
            middle = left_index + (right_index - left_index) // 2
            if nums[middle] == target:
                result = middle
                if left_bound:
                    right_index = middle - 1
                else:
                    left_index = middle + 1
            elif nums[middle] < target:
                left_index = middle + 1
            else:
                right_index = middle - 1
        return result

    first_occurrence = binarySearch(nums, target, left_bound=True)
    last_occurrence = binarySearch(nums, target, left_bound=False)

    return [first_occurrence, last_occurrence]


nums = [5,7,7,8,8,10]
target = 8
result = searchingRange(nums, target)
print(result)
