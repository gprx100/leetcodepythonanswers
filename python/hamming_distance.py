class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = format(x,'b')
        by = format(y, 'b')
        if len(bx) > len(by):
            by = by.zfill(len(bx))
        else:
            bx = bx.zfill(len(by))
        count = 0
        for pos in range(0,len(by)):
            if by[pos] != bx[pos]:
                count += 1
        return count
