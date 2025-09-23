# # LeetCode Problem 283: Move Zeroes
# # Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# # Note that you must do this in-place without making a copy of the array. 


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0

        # Move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1

        # Fill the remaining positions with 0
        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0
