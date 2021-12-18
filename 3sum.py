class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        List = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    for k in range(len(nums)):
                        if j != k and k != i:
                            tmp = nums[i] + nums[j] + nums[k]
                            if tmp == 0:
                                sortedItem = sorted([nums[i], nums[j], nums[k]])
                                if not(sortedItem in List):
                                    List.append(sortedItem)
        return List
