class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        ret = []
        for i in xrange(numRows):
            if i == 0:
                ret.append([1])
            else:
                ret.append([j for j in xrange(i + 1)])
                ret[i][0] = 1
                ret[i][-1] = 1
                for p, _ in enumerate(ret[i][1:-1]):
                    ret[i][p + 1] = ret[i - 1][p] + ret[i - 1][p + 1]
        return ret
