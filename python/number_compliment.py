class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        base2 =  "{0:b}".format(num)
        print base2
        comp = []
        for b in base2:
            if b == '0':
                comp.append('1')
            elif b == '1':
                comp.append('0')
        c = ''.join(comp)
        return int(c, 2)
