from collections import defaultdict
from typing import List

class Solution:
    def sieve_of_eratosthenes(self, n):
        # 初始化一个布尔数组，用于标记每个数是否为质数
        is_prime = [True] * n

        # 0和1不是质数，将它们标记为False
        is_prime[0] = is_prime[1] = False

        # 遍历2到sqrt(n)，标记倍数为非质数
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        # 收集所有质数
        primes = [i for i in range(n) if is_prime[i]]
        primes = {i: 1 for i in primes}
        return primes

    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n <= 2:
            return []
        all_p = self.sieve_of_eratosthenes(n)
        used = defaultdict(int)
        ans = []
        for num1 in all_p.keys():
            if all_p.get(n - num1) and not used[num1] and not used[n - num1]:
                ans.append([num1, n - num1])
                used[num1] = 1
                used[n - num1] = 1
        return ans



sl = Solution()
cases = [10, 2]
for n in cases:
    print(sl.findPrimePairs(n))