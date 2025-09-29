# Leet code 151: Reverse Words in a String

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        left, right = 0, n-1
        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1

        tmp = []
        while left <= right:
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ':
                tmp.append(' ')
            left += 1

        def reverse(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        reverse(tmp, 0, len(tmp)-1)

        start = 0
        for i in range(len(tmp)+1):
            if i == len(tmp) or tmp[i] == ' ':
                reverse(tmp, start, i-1)
                start = i + 1

        return "".join(tmp)