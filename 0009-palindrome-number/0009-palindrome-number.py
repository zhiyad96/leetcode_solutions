class Solution(object):
    def isPalindrome(self, x):
        result=True
        x=str(x)
        for i in range(len(x)//2):
            if x[i]==x[len(x)-1-i]:
                continue
            else:
                result=False
        return result
            