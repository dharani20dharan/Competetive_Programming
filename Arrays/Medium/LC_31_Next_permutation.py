# Leet code 31 : Next Permutation

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # Step 1: Find the first decreasing element from the end
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find the element just larger than nums[i] to swap with
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the elements after index i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    