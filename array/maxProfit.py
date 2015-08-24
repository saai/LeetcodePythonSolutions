class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_v = sys.maxint
        max_v = -sys.maxint-1
        max_profit = 0
        for p in prices:
            if p < min_v :
                min_v = p
                max_v = p
            elif p > max_v:
                max_v = p
            if max_profit < (max_v - min_v):
                max_profit = max_v - min_v
        return max_profit
                