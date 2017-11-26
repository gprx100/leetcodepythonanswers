class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        strdigits = ''.join(str(d) for d in digits)
        num = int(strdigits) + 1
        strdigits = ''.join(d for d in str(num))
        for d in strdigits:
            res.append(int(d))
        return res
