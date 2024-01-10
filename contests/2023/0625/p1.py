from typing import List

class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def are_co_primes(self, a, b):
        return self.gcd(a, b) == 1
    def get_first_digit(self, n):
        while n >= 10:
            n //= 10
        return n
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if self.are_co_primes(self.get_first_digit(nums[i]), nums[j] % 10):
                    ans += 1
        return ans

params = (([11,21,12], 2))
sl = Solution()
for case in params:
    nums, ans = case
    print(f"{sl.countBeautifulPairs(nums)} {ans}")