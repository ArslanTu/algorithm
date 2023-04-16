from typing import List
from collections import Counter

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:


        # def is_prime(x):
        #     if (x == 2) or (x == 3):
        #         return True
        #     if (x % 6 != 1) and (x % 6 != 5):
        #         return False
        #     for i in range(5, int(x ** 0.5) + 1, 6):
        #         if (x % i == 0) or (x % (i + 2) == 0):
        #             return False
        #     return True

        def is_prime(n):
            if n <= 1:
                return False
            elif n <= 3:
                return True
            elif n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        ans = 0
        n = len(nums)
        for i in range(n):
            if is_prime(nums[i][i]):
                ans = max(ans, nums[i][i])
            if is_prime(nums[i][n - i - 1]):
                ans = max(ans, nums[i][n - i - 1])
        return ans


sl = Solution()

p1 = 

print(sl)