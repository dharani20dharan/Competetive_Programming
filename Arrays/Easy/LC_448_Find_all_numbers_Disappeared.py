# Leetcode 448 : Find all numbers disappeared in an Array

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        return list(set(range(1, n+1)) - set(nums))