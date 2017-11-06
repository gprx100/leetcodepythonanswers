class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n%2 == 0:
                if n/2 == 1:
                    return True
                else:
                    n = n/2
                    continue
            else:
                return False
        if n == 1:
            return True
        if n== 0 or n < 0:
            return False
