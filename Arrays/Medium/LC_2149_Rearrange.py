# Leetcode 2149 : Rearrange Array Elements by Sign

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        
        result = []
        for p, n in zip(pos, neg):
            result.append(p)
            result.append(n)
        
        return result
