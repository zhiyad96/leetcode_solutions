class Solution(object):
    def averageValue(self, nums):
        sum=0
        count=0
        for x in nums:
            if x%2==0:
                if x%3==0:
                    sum+=x
                    count+=1
        if sum==0:
            return 0
        else:
            return sum//count