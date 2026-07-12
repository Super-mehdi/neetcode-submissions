def findMinHelper(nums,l,r):
    if l==r:
        return nums[l]
    mid = l+(r-l)//2
    if nums[mid]<nums[r]:
        return findMinHelper(nums,l,mid)
    return findMinHelper(nums,mid+1,r)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if (n==1):
            return nums[0]
        return findMinHelper(nums,0,n-1)