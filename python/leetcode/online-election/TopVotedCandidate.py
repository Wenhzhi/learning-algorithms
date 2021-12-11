# 911. 在线选举
# https://leetcode-cn.com/problems/online-election/

from typing import List
from collections import defaultdict

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        tops = []
        voteCounts = defaultdict(int)
        voteCounts[-1] = -1
        top = -1
        for p in persons:
            voteCounts[p] += 1
            if voteCounts[p] >= voteCounts[top]:
                top = p
            tops.append(top)
        self.tops = tops
        self.times = times

    def q(self, t: int) -> int:
        l, r = 0, len(self.times) - 1
        # 找到满足 times[l] <= t 的最大的 l
        while l < r:
            m = l + (r - l + 1) // 2
            if self.times[m] <= t:
                l = m
            else:
                r = m - 1
        # 也可以使用内置的二分查找的包来确定 l
        # l = bisect.bisect(self.times, t) - 1
        return self.tops[l]


if __name__ == '__main__':
    import sys
    import io
    import json
    def readLines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    line = readLines()
    while True:
        try:
            commands = json.loads(next(line))
            nums = json.loads(next(line))
            result = []
            topVotedCandidate = TopVotedCandidate(nums[0][0], nums[0][1])
            for i, p in enumerate(commands):
                if p == "TopVotedCandidate":
                    result.append("null")
                elif p == "q":
                    print(i, ": ", nums[i][0])
                    result.append(topVotedCandidate.q(nums[i][0]))

            print("result: ", result)
        except StopIteration:
            break
