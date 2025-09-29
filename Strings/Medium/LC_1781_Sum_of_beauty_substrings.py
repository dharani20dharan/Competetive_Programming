# Leet code 1781: Sum Of Beauty Of All Substrings

class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        total = 0

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1

                max_freq = max(freq)
                min_freq = min(f for f in freq if f> 0)
                total += max_freq - min_freq

        return total
