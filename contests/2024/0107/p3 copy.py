from typing import *

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        to_delete1 = len(nums1) // 2
        to_delete2 = to_delete1
        for key in counter1.keys():
            val = counter1[key]
            if val > 1:
                to_delete1 -= val - 1
                counter1[key] = 1
        for key in counter2.keys():
            val = counter2[key]
            if val > 1:
                to_delete2 -= val - 1
                counter2[key] = 1

        if to_delete1 <= 0 and to_delete2 <= 0:
            s1 = set([num if counter1[num] > 0 else 0 for num in counter1.keys()])
            s2 = set([num if counter2[num] > 0 else 0 for num in counter2.keys()])
            s = s1.union(s2)

            try:
                s.remove(0)
            except KeyError:
                pass

            return len(s)

        if to_delete1 > 0:
            for num in counter1.keys():
                if counter2[num] > 0:
                    to_delete1 -= 1
                    counter1[num] = 0
                if to_delete1 <= 0:
                    break

        if to_delete2 > 0:
            for num in counter2.keys():
                if counter1[num] > 0:
                    to_delete2 -= 1
                    counter2[num] = 0
                if to_delete2 <= 0:
                    break

        s1 = set([num if counter1[num] > 0 else 0 for num in counter1.keys()])
        s2 = set([num if counter2[num] > 0 else 0 for num in counter2.keys()])
        s = s1.union(s2)

        try:
            s.remove(0)
        except KeyError:
            pass

        if to_delete1 <= 0 and to_delete2 <= 0:
            return len(s)
        else:
            ans = len(s)
            if to_delete1 > 0:
                ans -= to_delete1
            if to_delete2 > 0:
                ans -= to_delete2
            return ans
        

sl = Solution()
examples = [
    ([1,2,1,2],[1,1,1,1], 2),
    ([1,2,3,4,5,6], [2,3,2,3,2,3], 5),
    ([1,1,2,2,3,3], [4,4,5,5,6,6], 6),
    ([2,4,1,4], [10,2,4,10], 4),
]
for example in examples:
    nums1, nums2, ans = example
    print(f"Output: {sl.maximumSetSize(nums1, nums2)}, Ans: {ans}")