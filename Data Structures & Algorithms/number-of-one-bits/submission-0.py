class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        num = n
        while (num//2 != 0):
            res += num%2
            num //= 2
        res += num
        return res