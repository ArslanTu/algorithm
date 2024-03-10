from typing import *


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:

        def gen(s: str):
            s_len = len(s)
            for i in range(s_len):
                for j in range(i, s_len):
                    yield s[i:j+1]
        
        ans = []
        n = len(arr)
        for i in range(n):
            cur_s = arr[i]
            cur_ans = None
            for s in gen(cur_s):
                if all([s not in arr[j] for j in range(n) if j != i]):
                    if cur_ans is None:
                        cur_ans = s
                    elif len(s) < len(cur_ans):
                        cur_ans = s
                    elif len(s) == len(cur_ans) and s < cur_ans:
                        cur_ans = s
            ans.append(cur_ans if cur_ans is not None else "")
        return ans


sl = Solution()
examples = [
    (["cab","ad","bad","c"], ["ab","","ba",""]),
    (["abc","bcd","abcd"], ["","","abcd"])
]
for example in examples:
    arr, ans = example
    print(f"Output: {sl.shortestSubstrings(arr)}, Ans: {ans}")