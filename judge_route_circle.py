class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        CL = 0
        CD = 0
        CU = 0
        CR = 0
        for m in moves:
            if m == 'U':
                CU += 1
            elif m == 'D':
                CD += 1
            elif m == 'L':
                CL += 1
            elif m == 'R':
                CR += 1
            else:
                return "Incorrect Input"
        if (CL - CR) == 0 and (CU - CD) == 0:
            return True
        else:
            return False
