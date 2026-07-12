def validAnagram(s,t):
    if (len(t) != len(s)) : return False
    counts = [0]*26
    for i in range(len(s)):
        counts[ord(s[i])-ord('a')]+=1
        counts[ord(t[i])-ord('a')]-=1
    for val in counts:
        if val != 0:
            return False
    return True


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =defaultdict(list)
        for s in strs:
            sortedS=''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
