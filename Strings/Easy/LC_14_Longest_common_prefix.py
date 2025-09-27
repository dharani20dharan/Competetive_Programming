# Leet Code 14: Longest Common Prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)

        def is_common_prefix(length):
            prefix = strs[0][:length]
            return all(s.startswith(prefix) for s in strs)
        low, high = 0, min_len
        while low < high:
            mid = (low + high + 1 ) // 2
            if is_common_prefix(mid):
                low = mid
            else:
                high = mid - 1
            
        return strs[0][:low]