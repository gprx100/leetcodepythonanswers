class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            for n in nums:
                if n > target:
                    return nums.index(n)
            return len(nums)
