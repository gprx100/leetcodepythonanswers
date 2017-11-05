class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = []
        for w in s.split():
            rs.append(w[::-1])
        return " ".join(rs)
