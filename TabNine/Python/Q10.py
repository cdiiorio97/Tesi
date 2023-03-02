class Solution(object):
    def maxProfit(self, prices):
        #You are given an array prices where prices[i] is the price of a given stock on the ith day.
        # Find the maximum profit you can achieve. You may complete at most two transactions.
        # Note: You may not engage in multiple transactions simultaneously 
        # (i.e., you must sell the stock before you buy again)
        #constraints: 1 <= prices.length <= 105 and 0 <= prices[i] <= 105
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
             return 0
        
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]



        return
    