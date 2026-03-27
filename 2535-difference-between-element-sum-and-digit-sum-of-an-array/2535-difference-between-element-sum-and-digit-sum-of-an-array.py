class Solution(object):
    def differenceOfSum(self, nums):
        res=0
        res1=0
        for i in nums:
            res+=i
            for j in str(i):
                res1+=int(j)

        result=res-res1
        return result
        