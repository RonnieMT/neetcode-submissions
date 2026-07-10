class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 1 

        l = 0

        if(s == ""):
            return 0

        currSet = set()
        currLen = 1
        for r in range(len(s)):
            while s[r] in currSet:
                currSet.remove(s[l])
                l += 1
            currSet.add(s[r])
            ans = max(ans, r - l + 1)

        return ans