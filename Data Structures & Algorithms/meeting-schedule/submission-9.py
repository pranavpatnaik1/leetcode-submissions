"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        if len(intervals) > 1:
            start, end = intervals[0].start, intervals[0].end 
        else:
            return True
        
        for i in range(1, len(intervals)):
            if intervals[i].start < end:
                return False
            start, end = intervals[i].start, intervals[i].end 
        
        return True