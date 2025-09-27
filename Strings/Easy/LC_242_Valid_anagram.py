# Leet Code 242: Valid Anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        return count_s == count_t