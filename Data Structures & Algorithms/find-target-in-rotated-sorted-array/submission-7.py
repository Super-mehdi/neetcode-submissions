class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if (n==1):
            return 0 if nums[0]==target else -1
        targetIndex = -1
        l,r=0,n-1
        while l<r:
            mid = l + (r-l)//2
            print(nums[l:r+1],mid)
            if target == nums[mid] :
                targetIndex = mid
                break
            elif nums[l] <= nums[mid]:
                if nums[l]<=target<=nums[mid] :
                    r = mid-1
                else:
                    l = mid + 1
                continue
            if nums[mid] <= nums[r] :
                if nums[mid]<=target<=nums[r] :
                    l = mid +1
                else :
                    r = mid -1
        if targetIndex==-1 and nums[l]==target:
            targetIndex = l
        return targetIndex
