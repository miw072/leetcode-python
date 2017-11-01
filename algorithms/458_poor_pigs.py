import math

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        states = minutesToTest / minutesToDie + 1
        return int(math.ceil(math.log(buckets, states)))
