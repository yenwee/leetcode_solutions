class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans = [[intervals[0][0], intervals[0][1]]]
        for index in range(len(intervals)):
            if ans[-1][1] >= intervals[index][0]:
                ans[-1][1] =  max(ans[-1][1], intervals[index][1])
            else:
                ans.append([intervals[index][0],intervals[index][1]])
        return ans