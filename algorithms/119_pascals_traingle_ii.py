class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == None or rowIndex < 0:
            return []

        if rowIndex == 0:
            return [1]

        ret = []
        prev = [1]
        for i in xrange(1, rowIndex + 1):
            ret = [j for j in xrange(i + 1)]
            ret[0] = 1
            ret[-1] = 1
            for p, _ in enumerate(ret[1:-1]):
                ret[p + 1] = prev[p] + prev[p + 1]
            prev = ret
        return ret

