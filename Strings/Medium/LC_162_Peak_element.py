# Leet Code 162: Find Peak Element

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
        
            if nums[mid] < nums[mid + 1]:
            # Peak must be on the right side
                left = mid + 1
            else:
            # Peak is on the left side (including mid)
                right = mid
    
        return left   
        