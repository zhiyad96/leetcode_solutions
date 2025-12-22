class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        cdepth=0
        mdepth=0
        for x in s :
            if x == "(":
                cdepth+=1
            elif x == ")":
                cdepth-=1
            if cdepth>mdepth:
                    mdepth+=1
        return mdepth


        