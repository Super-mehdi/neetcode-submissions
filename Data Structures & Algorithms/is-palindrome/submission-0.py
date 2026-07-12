class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        print(s)
        n = len(s)
        i,j = 0,n-1
        while i < j :
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True