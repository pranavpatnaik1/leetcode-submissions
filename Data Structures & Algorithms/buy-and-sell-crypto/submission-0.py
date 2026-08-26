class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxP = 0
        while r < len(prices):
            maxP = max(prices[r] - prices[l], maxP)

            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return maxP
