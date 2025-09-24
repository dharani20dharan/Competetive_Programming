# Leet Code 219 : Contains Duplicate II

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}

        for i, num in enumerate(nums):
            if num in seen:
                if i - seen[num] <= k:
                    return True

            seen[num] = i

        return False