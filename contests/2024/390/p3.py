from collections import defaultdict
from typing import *
from sortedcontainers import SortedDict


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        id2cnt = defaultdict(int)
        cnt2ids = SortedDict()
        ans = []
        for id, f in zip(nums, freq):
            origin_cnt = id2cnt[id]
            if origin_cnt in cnt2ids:
                if id in cnt2ids[origin_cnt]:
                    cnt2ids[origin_cnt].remove(id)
                    if len(cnt2ids[origin_cnt]) == 0:
                        del cnt2ids[origin_cnt]
            id2cnt[id] += f
            if id2cnt[id] not in cnt2ids:
                cnt2ids[id2cnt[id]] = set()
            cnt2ids[id2cnt[id]].add(id)
            ans.append(cnt2ids.peekitem(-1)[0])
        return ans


sl = Solution()
examples = [
    ([2,3,2,1], [3,2,-3,1], [3,3,2,2]),
    ([5,5,3], [2,-2,1], [2,0,1])
]
for example in examples:
    nums, freq, ans = example
    print(f"Output: {sl.mostFrequentIDs(nums, freq)}, Ans: {ans}")