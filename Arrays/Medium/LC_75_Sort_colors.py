# Leetcode 75 : Sort Colors


def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:  # red
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:  # white
            mid += 1
        else:  # nums[mid] == 2 (blue)
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
