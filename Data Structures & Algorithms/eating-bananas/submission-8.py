class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        best = r

        while l <= r:
            k = (l + r) // 2
            curr = 0
            for p in piles:
                curr += (p + k - 1) // k
            if curr <= h:
                best = k
                r = k - 1
            else:
                l = k + 1
        return best


