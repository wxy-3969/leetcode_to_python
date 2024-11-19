'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
'''

class Solution:
    def convert(self, s, numRows):
        n = len(s)
        # 边界情况处理
        if numRows == 1 or numRows >= n:
            return s
        ans = []
        # 周期
        t = numRows * 2 - 2
        for i in range(numRows):
            # 从0开始，步长为周期
            for j in range(0, n - i, t):
                ans.append(s[j + i])
                if i >= 1 and i < numRows - 1 and j - i + t < n:
                    ans.append(s[j - i + t])
        # 将列表转换为字符串
        return ''.join(ans)
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 4))

