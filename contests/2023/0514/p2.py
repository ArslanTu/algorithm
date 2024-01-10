from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        ans_1 = [0]
        for i in range(n - 1):
            ans_1.append(derived[i] ^ ans_1[-1])
        ver_1 = derived[-1] ^ ans_1[-1]
        if ver_1 == ans_1[0]:
            return True

        ans_2 = [1]
        for i in range(n - 1):
            ans_2.append(derived[i] ^ ans_2[-1])
        ver_2 = derived[-1] ^ ans_2[-1]
        if ver_2 == ans_2[0]:
            return True
    
        return False




sl = Solution()
p1 = [1, 1]
print(sl.doesValidArrayExist(p1))