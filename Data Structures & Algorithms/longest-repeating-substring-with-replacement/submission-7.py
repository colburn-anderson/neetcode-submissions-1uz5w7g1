class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        best = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best



