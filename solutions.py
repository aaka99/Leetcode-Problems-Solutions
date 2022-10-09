# 2432. The Employee That Worked on the Longest Task
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        res = logs[0][0]
        Max = logs[0][1]
        for i in range(1,len(logs)):
            if logs[i][1]-logs[i-1][1]>Max:
                res = logs[i][0]
                Max = logs[i][1]-logs[i-1][1]
            elif logs[i][1]-logs[i-1][1]==Max and res>logs[i][0]:
                res = logs[i][0]
        return res
