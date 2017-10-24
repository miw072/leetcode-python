class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        for i, price in enumerate(prices[1:]):
            if price > prices[i]:
                max_profit += (price - prices[i])
        return max_profit
