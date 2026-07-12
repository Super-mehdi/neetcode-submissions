class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)) : return False
        d = { x : 0 for x in set(s)}
        for i in range(len(s)):
            d[s[i]]+=1
            if (t[i] in d.keys()):
                d[t[i]]-=1
            else :
                return False
        for value in d.values():
            if (value != 0) : return False
        return True
