class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lp = prices[0]

        mp = 0

        for i in prices:
            mp = max(mp, i - lp)
            lp = min(i,lp)
        return mp