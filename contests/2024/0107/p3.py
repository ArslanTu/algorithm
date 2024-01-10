from typing import *

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        m1, m2 = len(nums1) // 2, len(nums2) // 2
        for num in cnt1.keys():
            cnt = cnt1[num]
            if cnt > 1:
                m1 -= cnt - 1
                cnt1[num] = 1
        for num in cnt2.keys():
            cnt = cnt2[num]
            if cnt > 1:
                m2 -= cnt - 1
                cnt2[num] = 1

        if m1 <= 0 and m2 <= 0:
            s1 = set([num if cnt1[num] > 0 else 0 for num in cnt1.keys()])
            s2 = set([num if cnt2[num] > 0 else 0 for num in cnt2.keys()])
            s = s1.union(s2)

            try:
                s.remove(0)
            except KeyError:
                pass

            return len(s)

        if m1 > 0:
            for num in cnt1.keys():
                if cnt2[num] > 0:
                    m1 -= 1
                    cnt1[num] = 0
                if m1 <= 0:
                    break

        if m2 > 0:
            for num in cnt2.keys():
                if cnt1[num] > 0:
                    m2 -= 1
                    cnt2[num] = 0
                if m2 <= 0:
                    break

        s1 = set([num if cnt1[num] > 0 else 0 for num in cnt1.keys()])
        s2 = set([num if cnt2[num] > 0 else 0 for num in cnt2.keys()])
        s = s1.union(s2)

        try:
            s.remove(0)
        except KeyError:
            pass

        if m1 <= 0 and m2 <= 0:
            return len(s)
        else:
            ans = len(s)
            if m1 > 0:
                ans -= m1
            if m2 > 0:
                ans -= m2
            return ans

sl = Solution()
examples = [
    # ([1,2,1,2],[1,1,1,1], 2),
    # ([1,2,3,4,5,6], [2,3,2,3,2,3], 5),
    # ([1,1,2,2,3,3], [4,4,5,5,6,6], 6),
    ([2,4,1,4], [10,2,4,10], 4),
]
for example in examples:
    nums1, nums2, ans = example
    print(f"Output: {sl.maximumSetSize(nums1, nums2)}, Ans: {ans}")