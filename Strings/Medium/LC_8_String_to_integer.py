# Leet Code 8 : String to integer

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s= s.lstrip()
        if not s:
            return 0

        sign = 1
        index = 0
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            index += 1

        num = 0
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1

        num *= sign

        INT_MIN, INT_MAX = -2**31, 2**31 -1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num