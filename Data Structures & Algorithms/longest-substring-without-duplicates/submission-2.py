class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charSet= set()
        l,r=0,0
        res = 0
        while l<n and r<n:
            if s[r] not in charSet:
                charSet.add(s[r])
                r += 1
            else :
                l += 1
                r=l
                charSet.clear()
            res = max(res,len(charSet))
        return res
            
        