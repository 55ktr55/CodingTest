class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minStartValue = nums[0]
        tmp = nums[0]
        for i in nums[1:]:
            tmp += i
            minStartValue = min(minStartValue, tmp)

        return (-1) * (minStartValue-1) if minStartValue < 0 else 1
