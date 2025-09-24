# Leet Code 209 : Minimum Size Subarray Sum
class Solution(object):
     def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        # Step 1: Sort the array to make it easier to find closest pairs
        arr.sort()
        
        # Step 2: Find the minimum absolute difference between consecutive elements
        min_diff = float("inf")
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]  # since arr is sorted, diff >= 0
            min_diff = min(min_diff, diff)
        
        # Step 3: Collect all pairs that have this minimum difference
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])
        
        return result