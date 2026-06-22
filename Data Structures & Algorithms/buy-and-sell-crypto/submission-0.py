class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l,r = 0,1
        while l < r and r < len(prices): 
            buyPrice = prices[l]
            sellPrice = prices[r]
            if sellPrice - buyPrice > maxProfit: 
                maxProfit = sellPrice - buyPrice
            if sellPrice < buyPrice: 
                l = r
            r += 1
        return maxProfit
            
        