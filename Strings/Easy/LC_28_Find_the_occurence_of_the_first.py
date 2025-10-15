# leet code 28 : Find the occurence of the first occurence of the string

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0  # empty needle found at index 0

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1