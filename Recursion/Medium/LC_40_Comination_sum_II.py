# Leet code 40: Combination sum II

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res= []
        candidates.sort()

        def backtrack(start, current, total):
            if total == target:
                res.append(list(current))
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])
                backtrack(i+1, current, total + candidates[i])
                current.pop()
        backtrack(0,[],0)
        return res