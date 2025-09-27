# Leet code 451 : Sort Characters By Frequency

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        sorted_chars = sorted(freq.items(), key = lambda x: x[1], reverse = True)

        result = ""
        for char, count in sorted_chars:
            result += char * count

        return result
        