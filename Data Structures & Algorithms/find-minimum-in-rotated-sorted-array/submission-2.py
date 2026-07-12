class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if (n==1):
            return nums[0]
        left = nums[:n//2]
        right = nums[n//2:]
        if left[-1]<= right[-1]:
            return self.findMin(left)
        return self.findMin(right)