from typing import *

class Solution:


    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        mapping = {}
        for idx, num in enumerate(nums):
            if num not in mapping:
                mapping[num] = [idx, -1]
            else:
                mapping[num][1] = idx
        n_pair = 0
        start = 0
        while start < n:
            end = mapping[nums[start]][1]
            if end == -1:
                n_pair += 1
                start += 1
            else:
                x = start + 1
                cur_end = end
                flag = True
                while flag:
                    flag = False
                    end = cur_end
                    for i in range(x, end):
                        if mapping[nums[i]][1] > cur_end:
                            cur_end = mapping[nums[i]][1]
                            flag = True
                            x = end
                n_pair += 1
                start = cur_end + 1
        return pow(2, n_pair - 1, 10 ** 9 + 7)


sl = Solution()
examples = [
    # ([1,2,3,4], 8),
    # ([1,1,1,1], 1),
    # ([1,2,1,3], 2),
    ([13,17,76,63,98,99,88,49,17,87,21,76,5,95,23,27,71,34,61,30,51,44,84,74,81,42,16,32,26,55,16,66,7,98,55,77,83,85,80,24,40,88,5,7,4,52,64,22,21,38,28,1,5,20,42,84,5,95,14,18,75,53,57,59,34,75,10,82,65,55,20,28,9,21,28,80,7,50,52,48,86,77,80,65,48,64,9,59,41,38,69,81,63,71,51,64,26,94,77,82], 2),
]
for example in examples:
    nums, ans = example
    print(f"Output: {sl.numberOfGoodPartitions(nums)}, Ans: {ans}")