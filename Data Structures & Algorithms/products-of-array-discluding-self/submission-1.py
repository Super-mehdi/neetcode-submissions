class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = []
        hasZero = False
        for num in nums :
            if num == 0 :
                if hasZero:
                    return [0]*len(nums)
                hasZero = True
                continue
            product *= num
        for i in range(len(nums)):
            if (nums[i]!=0 and not hasZero):
                nums[i]=product//nums[i]
            elif (nums[i]!=0 and hasZero):
                nums[i]=0
            else:
                nums[i]=product
        return nums
