"""
weekply contest p2
"""
from typing import *


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = list(set([tuple(x) for x in meetings]))
        meetings = [list(x) for x in meetings]
        meetings.sort(key=lambda x: x[0])
        meetings_t = [meetings[0]]
        for i in range(1, len(meetings)):
            if meetings[i][0] <= meetings_t[-1][1]:
                meetings_t[-1][1] = max(meetings_t[-1][1], meetings[i][1])
            else:
                meetings_t.append(meetings[i])
        total_work = sum(x[1] - x[0] + 1 for x in meetings_t)
        return days - total_work


def test():
    """
    test func
    """
    sl = Solution()
    examples = [
        (10, [[5, 7], [1, 3], [9, 10]], 2), (5, [[2, 4], [1, 3]], 1),
        (6, [[1, 6]], 0)
    ]
    for example in examples:
        days, meetings, ans = example
        print(f"Output: {sl.countDays(days, meetings)}, Ans: {ans}")


if __name__ == "__main__":
    test()
