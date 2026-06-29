class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countArr = {}

        for n in nums:
            countArr[n] = countArr.get(n, 0) + 1

        sortedNums = sorted(countArr.items(), key=lambda x: x[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(sortedNums[i][0])

        return ans