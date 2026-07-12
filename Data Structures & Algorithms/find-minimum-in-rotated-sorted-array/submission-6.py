class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if (n==1):
            return nums[0]
        l,r = 0,n-1
        mid = l+(r-l)//2
        while l<r:
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid+1
            mid = l+(r-l)//2
        return nums[l]