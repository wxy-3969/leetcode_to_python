'''
实现一个myAtoi(string)函数,使其能将字符串转换成一个32位有符号整数。
函数 myAtoi(string s) 的算法如下：
空格：读入字符串并丢弃无用的前导空格(" ")
符号：检查下一个字符（假设还未到字符末尾）为'-'还是'+'。如果两者都不存在，则假定结果为正。
转换：通过跳过前置零来读取该整数,直到遇到非数字字符或到达字符串的结尾。如果没有读取数字,则结果为0。
舍入：如果整数数超过 32 位有符号整数范围[-2^31, 2^31-1],需要截断这个整数,使其保持在这个范围内。
具体来说,小于-2^31的整数应该被舍入为 -2^31,大于 2^31-1的整数应该被舍入为 2^31-1 。
'''
class Solution:
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0
        # 判断正负号
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            index = 1
        num = 0
        # 遍历字符串
        for i in range(index, len(s)):
            if not s[i].isdigit():
                break
            # 计算数字
            num = num * 10 + int(s[i])
        num *= sign
        if num < -2**31:
            return -2**31
        elif num > 2**31 - 1:
            return 2**31 - 1
        return num
# 测试
if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi("42"))