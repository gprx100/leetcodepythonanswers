class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bn = format(n, 'b')
        return bn.count('1')
