class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for letter in ransomNote:
            if letter in magazine:
                nmagazine = magazine.replace(letter, '', 1)
                magazine = nmagazine
            else:
                return False
        return True
