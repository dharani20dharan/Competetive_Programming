# LeetCode Problem 66: Plus One 
# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list,           
# and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list,    
# and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Start from the last digit
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits were 9
        return [1] + digits
