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
                res = max(res,len(charSet))
            else :
                charSet.remove(s[l])
                l += 1
        return res
            
        