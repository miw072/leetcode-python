class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if not n:
            return ''

        ret = ''
        while n > 0:
            ret = chr(ord('A') + (n - 1) % 26) + ret
            n = (n - 1) / 26

        return ret
