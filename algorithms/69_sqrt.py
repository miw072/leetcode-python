class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == None:
            return None

        if x == 0:
            return 0

        left = 1
        right = x
        ret = None
        while left <= right:
            mid = left + (right - left) / 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
                ret = mid
        return ret
