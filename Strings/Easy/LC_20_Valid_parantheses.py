# Leet code 20 : Valid Paranthesis

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():  # if it's an opening bracket
                stack.append(char)
            else:  # it's a closing bracket
                if not stack:
                    return False
                top = stack.pop()
                if mapping[char] != top:
                    return False

        return len(stack) == 0
