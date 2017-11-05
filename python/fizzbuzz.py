class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        li = []
        for num in xrange(1,n+1):
            if (num % 3 == 0 and num % 5 == 0):
                li.append("FizzBuzz")
            elif num % 5 == 0:
                li.append("Buzz")
            elif num % 3 == 0:
                li.append("Fizz")
            else:
                li.append(str(num))
        return li
