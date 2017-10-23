class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0

        dic = {1: 1, 2: 2}
        for i in xrange(3, n + 1):
            dic[i] = dic[i - 1] + dic[i - 2]
        return dic[n]
