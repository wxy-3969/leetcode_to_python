'''
给定一个字符串s和一个字符规律p,请你来实现一个支持'.'和'*'的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配,是要涵盖整个字符串s的,而不是部分字符串。
'''


class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        def match(i, j):    # 辅助函数，判断当前字符是否匹配
            if j == 0:
                return False
            if p[j - 1] == '.':
                return i > 0
            return i > 0 and s[i - 1] == p[j - 1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):    # 处理模式p为空字符串能匹配空字符串s的情况，及以'*'开头时的初始化
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1]!= '*':
                    dp[i][j] = dp[i - 1][j - 1] and match(i, j)    # 当前字符非'*',依赖前一个字符匹配情况及整体匹配情况
                else:
                    # 当前字符是'*'，分两种情况处理
                    dp[i][j] = dp[i][j - 2]  # '*'匹配零个前面元素的情况
                    if match(i, j - 1):
                        dp[i][j] = dp[i][j] or dp[i - 1][j]  # '*'匹配一个或多个前面元素的情况
        return dp[m][n]
# 测试
if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch("aa", "a"))