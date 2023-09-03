def medianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m
    median = 0.0

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1

        maximumLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minimumRight1 = float('inf') if partition1 == m else nums1[partition1]

        maximumLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minimumRight2 = float('inf') if partition2 == n else nums2[partition2]

        if maximumLeft1 <= minimumRight2 and maximumLeft2 <= minimumRight1:
            if (m + n) % 2 == 0:
                median = (max(maximumLeft1, maximumLeft2) + min(minimumRight1, minimumRight2)) / 2.0
            else:
                median = max(maximumLeft1, maximumLeft2)
            break
        elif maximumLeft1 > minimumRight2:
            right = partition1 - 1
        else:
            left = partition1 + 1

    return median
nums1 = [1, 3]
nums2 = [2]
result = medianSortedArrays(nums1, nums2)
print(result)
