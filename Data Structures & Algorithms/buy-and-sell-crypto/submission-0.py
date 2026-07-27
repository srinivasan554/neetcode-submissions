class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        best_min = float('inf')

        max_profit = 0
        
        for price in prices:
            best_min = min(best_min, price)

            max_profit = max(max_profit , price - best_min )

        return max_profit