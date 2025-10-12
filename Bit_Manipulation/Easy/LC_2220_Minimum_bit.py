# Leet code 2220 : Minimum bit flips to convert

class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        # 1. Use the XOR operator to find a number representing all the differing bits.
        #    A '1' in the result means that bit needs to be flipped.
        differing_bits = start ^ goal
        
        # 2. Convert the result to its binary string representation (e.g., '0b1101')
        #    and count the number of '1's. This count is the answer.
        return bin(differing_bits).count('1')
        