class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # variable to capture uppercase count
        ucount = 0
        for ch in word:
            if ch.isupper():
                ucount += 1
        print(ucount)
        if ucount == 0:
            return True
        if ucount == len(word):
            return True
        if ucount == 1 and word[0].isupper():
            return True
        return False
