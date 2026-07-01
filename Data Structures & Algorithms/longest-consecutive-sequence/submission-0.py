class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)


        ans = 0

        for n in setNums:
            currMax = 0
            if n - 1 not in setNums:
                nextNum = n
                while nextNum in setNums:
                    currMax += 1
                    nextNum += 1
                ans = max(ans, currMax)

        return ans
            