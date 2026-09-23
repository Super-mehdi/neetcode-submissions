class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = intervals[:]
        n = len(res)

        for i in range(n):
            if res[i][0]>=newInterval[0]:
                res.insert(i,newInterval)
                break
        if len(res) == n:
            res.append(newInterval)
        mergedRes = []
        for interval in res:
            if not mergedRes or mergedRes[-1][1] < interval[0]:
                mergedRes.append(interval)
            else:
                mergedRes[-1][1] = max(mergedRes[-1][1],interval[1])

        return mergedRes


        