# Leet code 58: Length of Last Word

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove trailing spaces and split the string
        words = s.strip().split()
        
        # Get the last word and return its length
        return len(words[-1])
