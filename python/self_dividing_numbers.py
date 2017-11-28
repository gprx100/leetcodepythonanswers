class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []

        for n in range(left, right+1):
            ds = str(n)
            count = 0
            for d in ds:
                if '0' in ds:
                    break
                if int(ds)%int(d) == 0:
                    count+= 1
            if count == len(ds):
                res.append(n)
        return res
