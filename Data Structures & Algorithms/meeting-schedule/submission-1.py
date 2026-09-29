"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key=lambda x: x.start)
        currentInterval = intervals[0]
        for interval in intervals[1:]:
            if interval.start < currentInterval.end:
                return False
            currentInterval = interval
        return True

