class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        currentInterval = intervals[0]
        cnt = 0
        for interval in intervals[1:]:
            if interval[0] < currentInterval[1]:
                cnt += 1
                currentInterval = min(currentInterval, interval, key=lambda x: x[1])
            else:
                currentInterval = interval
        return cnt