class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]*(n+1)
        for i in range(1,n+1):
            cnt = 0
            num = i
            while num != 0:
                cnt += num%2
                num //= 2
            output[i] = cnt
        return output
