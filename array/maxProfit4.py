class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<=1:
            return 0
        if (k >= n / 2):
            return self.quickSolve(prices)
        dp = [[0 for j in xrange(n)] for i in xrange(k+1)]
        for i in range(1,k+1):
            temp = dp[i-1][0] - prices[0]
            for j in xrange(1,n):
                dp[i][j] = max(dp[i][j-1], temp+prices[j]) # equals to i-1 th transaction or sell to complete new transaction.
                temp = max(temp, dp[i-1][j]-prices[j])
        return dp[k][n-1]

    def quickSolve(self, prices):
        profits = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profits += (prices[i]-prices[i-1])
        return profits