class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = 0
        min_v = -1
        max_v = -1
        n = len(prices)
        for i in range(n):
            p = prices[i]
            if p < min_v or min_v == -1:
                min_v = p
                max_v = p
            elif p > max_v:
                max_v = p
            if i>0 and p>prices[i-1]:      
                profits = max((profits+p-prices[i-1]),p-min_v)
        return profits