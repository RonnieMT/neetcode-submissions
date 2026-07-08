class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        l = 0
        r = 1

        currLowest = 0
        currHighest = 0

        while r < len(prices):
            leftPrice = prices[l]
            rightPrice = prices[r]

            if leftPrice >= rightPrice:
                l = r
            
            r += 1
            
            ans = max(ans, (rightPrice - leftPrice))

        return ans