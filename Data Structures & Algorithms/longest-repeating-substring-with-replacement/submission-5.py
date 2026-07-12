class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0: return 0
        res = 0
        l = 0
        while l < n:
            r = l + 1
            handle = k
            while r < n:
                if s[r] != s[l]:
                    if handle > 0:
                        handle -= 1
                    else:
                        break
                r += 1
            res = max(res, min(n, r - l + handle))
            l += 1
        return res