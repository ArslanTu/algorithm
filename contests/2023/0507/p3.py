from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums = [0] * n
        ans = [0]
        for idx, c in queries:
            if nums[idx] == c:
                ans.append(ans[-1])
                continue
            ori_c = nums[idx]
            nums[idx] = c
            ans.append(ans[-1])
            if idx > 0:
                if nums[idx - 1] != 0 and nums[idx - 1] == ori_c:
                    ans[-1] -= 1
                else:
                    if nums[idx - 1] == c:
                        ans[-1] += 1
            if idx < n - 1:
                if nums[idx + 1] != 0 and nums[idx + 1] == ori_c:
                    ans[-1] -= 1
                else:
                    if nums[idx + 1] == c:
                        ans[-1] += 1
        return ans[1:]