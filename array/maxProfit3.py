class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1 = hold2 = -sys.maxint -1
        release1 = release2 = 0
        for p in prices:
            release2 = max(release2,hold2+p)
            hold2 = max(hold2, release1-p)
            release1 = max(release1, hold1+p)
            hold1 = max(hold1,-p)
        return release2
        