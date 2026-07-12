class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = float('inf')
        for num in nums:
            if num < minNum:
                minNum = num
        return minNum