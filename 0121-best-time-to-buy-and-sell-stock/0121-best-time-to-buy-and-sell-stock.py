class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Find the best buying price
            if price < min_price:
                min_price = price
            
            # Calculate profit if sold today
            profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit

        return max_profit