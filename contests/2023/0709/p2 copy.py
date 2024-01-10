from typing import List

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums3 = []
        for i in range(len(nums1) - 1, -1, -1):
            if i == len(nums1) - 1 or max(nums1[i], nums2[i]) <= nums3[-1]:
                nums3.append(max(nums1[i], nums2[i]))
            else:
                if min(nums1[i], nums2[i]) <= nums3[-1]:
                    nums3.append(min(nums1[i], nums2[i]))
                else:
                    nums3.append(max(nums1[i], nums2[i]))
        nums3 = nums3[::-1]
        ans = 0
        cur = 1
        for i in range(len(nums3)):
            if i > 0 and nums3[i] >= nums3[i-1]:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 1
        ans = max(ans, cur)

        nums3 = []
        for i in range(len(nums1)):
            if i == 0 or min(nums1[i], nums2[i]) >= nums3[-1]:
                nums3.append(min(nums1[i], nums2[i]))
            else:
                if max(nums1[i], nums2[i]) >= nums3[-1]:
                    nums3.append(max(nums1[i], nums2[i]))
                else:
                    nums3.append(min(nums1[i], nums2[i]))
        cur = 1
        for i in range(len(nums3)):
            if i > 0 and nums3[i] >= nums3[i-1]:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 1
        ans = max(ans, cur)
        return ans


sl = Solution()
use_cases = [([2,3,1], [1,2,1], 2), ([1,3,2,1], [2,2,3,4], 4), ([1,1], [2,2], 2), ([8,7,4], [13,4,4], 2), ([11,7,7,9], [19,19,1,7], 3), ([4,16,10,8], [8,4,1,9], 3), ([16,9,5,7,2,6], [9,5,2,5,19,12], 4)]
for use_case in use_cases:
    nums1, nums2, ans  = use_case
    print(f"{sl.maxNonDecreasingLength(nums1, nums2)}, {ans}")

    

