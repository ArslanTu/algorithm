from typing import *
from sortedcontainers import SortedList

class Solution:
    def maximumLength(self, s: str) -> int:
        chs = set(s)
        ans = -1

        for ch in chs:
            len_cnt = []
            cnt = 0
            for c in s:
                if c == ch:
                    cnt += 1
                else:
                    if cnt > 0:
                        len_cnt.append(cnt)
                    cnt = 0
            if cnt > 0:
                len_cnt.append(cnt)
            len_cnt.sort()

            def check(ss):
                if len(ss) > len_cnt[-1]:
                    return False
                cnt = 0
                for i in range(len(len_cnt) - 1, -1, -1):
                    if cnt >=3 or len_cnt[i] < len(ss):
                        break
                    else:
                        cnt += len_cnt[i] - (len(ss) - 1)
                return cnt >= 3
            
            low, high = 1, len_cnt[-1]
            while low <= high:
                mid = (low + high) // 2
                if check(ch * mid):
                    ans = max(ans, mid)
                    low = mid + 1
                else:
                    high = mid - 1
        return ans


sl = Solution()
examples = [
    ("aaaa", 2),
    ("abcdef", -1),
    ("abcaba", 1),
]
for example in examples:
    s, ans = example
    print(f"Output: {sl.maximumLength(s)}, Ans: {ans}")