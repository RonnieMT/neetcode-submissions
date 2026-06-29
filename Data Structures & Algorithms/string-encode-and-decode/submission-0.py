class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for s in strs:
            ans += s
            ans += "\n"

        return ans

    def decode(self, s: str) -> List[str]:
        
        ans = s.splitlines()

        return ans