# leet code 216 : Combination sum III

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(start, comb, total):
            if len(comb) == k and total == n:
                res.append(comb[:])
                return

            if len(comb) > k or total > n:
                return

            for i in range(start, 10):
                comb.append(i)
                backtrack(i + 1, comb, total + i)
                comb.pop()

        backtrack(1, [], 0)
        return res
