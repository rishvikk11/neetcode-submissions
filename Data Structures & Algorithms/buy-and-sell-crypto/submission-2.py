class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        max_profit = 0
        
        for i in range(len(prices)):
            if i == 0:
                min_buy_price = prices[i]
                continue
            max_profit = max(max_profit, prices[i]-min_buy_price)
            min_buy_price = min(min_buy_price, prices[i])

        return max_profit            