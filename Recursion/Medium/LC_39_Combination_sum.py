# Leet code 39 : Combination sum

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(start,current, total):
            if total == target:
                res.append(list(current))
                return
            
            if total > target:
                return
            
            for i in range (start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])
                current.pop()

            
        backtrack(0,[], 0)
        return res