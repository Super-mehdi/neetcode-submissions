class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        hasZero = False
        res = []
        for num in nums :
            if num == 0 :
                if hasZero:
                    return [0]*len(nums)
                hasZero = True
                continue
            product *= num
        for num in nums:
            if hasZero and num != 0 :
                res.append(0)
            elif hasZero and num == 0:
                res.append(product)
            else :
                res.append(product//num)
        return res
