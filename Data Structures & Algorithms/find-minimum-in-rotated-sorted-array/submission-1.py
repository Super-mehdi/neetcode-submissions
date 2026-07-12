class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if (n==2):
            return nums[0] if nums[0]<=nums[1] else nums[1]
        elif (n==1):
            return nums[0]
        left = self.findMin(nums[:n//2]) 
        right = self.findMin(nums[n//2:]) 
        return min(left,right)