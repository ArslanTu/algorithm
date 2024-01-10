class Solution:
    def punishmentNumber(self, n: int) -> int:

        def is_valid(num_str, start, end, target):
            if start > end:
                return target == 0
            for i in range(start, end+1):
                cur = int(num_str[start:i+1])
                if cur <= target and is_valid(num_str, i+1, end, target-cur):
                    return True
            return False


        res = 0
        for i in range(1, n+1):
            num_str = str(i*i)
            if is_valid(num_str, 0, len(num_str)-1, i):
                res += i*i
        return res

print(get_punish_num(1000))