class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l,r = 0,n-1
        maxWaterAmount = 0
        while l < r :
            currentWaterAmount = min(heights[l],heights[r]) * (r-l)
            maxWaterAmount = max(maxWaterAmount,currentWaterAmount)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxWaterAmount
            


