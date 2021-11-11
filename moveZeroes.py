class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        initLength = len(nums)
        nZero = 0
        for i in range(initLength):
            if nums[i-nZero] == 0:
                nums.append(nums.pop(i-nZero))
                nZero += 1

        return nums
