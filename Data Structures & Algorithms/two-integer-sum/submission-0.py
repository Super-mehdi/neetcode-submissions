class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = set(nums)
        n = len(nums)
        possible = []
        for i in range(n):
            if target - nums[i] in numSet:
                possible.append(i)
        i = 0
        while (len(possible) > 2 and i < len(possible)-1):
            if (nums[possible[i]]*2 == target):
                print("here")
                possible.pop(i)
                return possible
            i+=1
        return possible