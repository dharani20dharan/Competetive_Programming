# Leet Code 151 : Reverse words in a String

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()

        words.reverse()

        return " ".join(words)