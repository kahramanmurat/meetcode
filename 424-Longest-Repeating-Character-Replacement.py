class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        countS = {}
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            while (r - l + 1) - max(countS.values()) > k:
                countS[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


s = "AABABBA"
k = 1
print(Solution.characterReplacement(self=s, s=s, k=k))
