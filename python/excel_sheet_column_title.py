import string

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        di = {}
        alph = list(string.uppercase)
        total = 0
        for i, val in enumerate(s):
            index = alph.index(val) + 1
            print index
            total += index*(26**(len(s)-(i+1)))
        return total
