class Solution(object):
    def returnToBoundaryCount(self, nums):
        position=0
        count=0
        for x in nums:
            position+=x
            if position==0:
                count+=1
        return count