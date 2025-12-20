class Solution(object):
    def getConcatenation(self, nums):
        for x in range(len(nums)):
            nums.append(nums[x])
        return nums
        
        