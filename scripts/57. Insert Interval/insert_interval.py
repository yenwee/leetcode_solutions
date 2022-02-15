class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        ans = [[intervals[0][0], intervals[0][1]]]
        for index in range(len(intervals)):
            if ans[-1][1] >= intervals[index][0]:
                ans[-1][1] =  max(ans[-1][1], intervals[index][1])
            else:
                ans.append([intervals[index][0],intervals[index][1]])
        return ans