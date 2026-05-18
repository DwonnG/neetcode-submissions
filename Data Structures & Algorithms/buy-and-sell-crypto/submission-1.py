class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        for right, price in enumerate(prices):
            if prices[left] > price:
                left = right
            possible = price - prices[left]
            profit = max(profit, possible)
        return profit