class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {x : False for x in nums} 
        for x in nums:
            if (d[x]):
                return True
            d[x] = True
        return False
