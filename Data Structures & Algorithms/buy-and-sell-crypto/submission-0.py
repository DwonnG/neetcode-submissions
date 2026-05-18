class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lp = 0
        for rp, price in enumerate(prices):
            if prices[lp] > prices[rp]:
                lp = rp
            profit = max(profit, prices[rp] - prices[lp])
        return profit
           
        