#
# @lc app=leetcode.cn id=1255 lang=python3
#
# [1255] 得分最高的单词集合
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # 状态压缩
        # n = len(words)
        # words_cnt = []
        # words_score = []
        # for word in words:
        #     sc = 0
        #     cnt = [0] * 26
        #     for ch in word:
        #         cnt[ord(ch) - 97] += 1
        #         sc += score[ord(ch) - 97]
        #     words_cnt.append(cnt)
        #     words_score.append(sc)
        # letters_cnt = [0] * 26
        # ans = 0
        # for letter in letters:
        #     letters_cnt[ord(letter) - 97] += 1
        # for case in range(1 << 14):
        #     cnt = [0] * 26
        #     res = 0
        #     for i in range(n):
        #         if ((case >> i) & 1) == 1:
        #             res += words_score[i]
        #             for j in range(26):
        #                 cnt[j] += words_cnt[i][j]
        #     success = True
        #     for k in range(26):
        #         if cnt[k] > letters_cnt[k]:
        #             success = False
        #             break
        #     if success:
        #         ans = max(ans, res)
        # return ans
        
        # 直接使用 Counter 的运算符
        n, ans = len(words), 0
        words_cnt = [Counter(word) for word in words]
        letters_cnt = Counter(letters)
        for case in range(1 << n):
            case_cnt = Counter()
            for i in range(n):
                if ((case >> i) & 1):
                    case_cnt += words_cnt[i]
            if case_cnt <= letters_cnt:
                ans = max(ans, sum(v * score[ord(k) - 97] for k, v in case_cnt.items()))
        return ans
# @lc code=end

