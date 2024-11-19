'''
给你一个 32 位的有符号整数x返回将x中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围-2^31~2^31-1就返回0。
'''
class Solution():
    def reverse(self,x):
        sign = 1 if x >= 0 else -1
        x = abs(x)
        reversed_num = 0
        # 循环，每次取出x的最后一位，然后放到reversed_num的末尾，直到x为0
        while x!= 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        reversed_num *= sign
        # 判断反转后的数字是否在32位有符号整数范围内
        if -2**31 <= reversed_num <= 2**31 - 1:
            return reversed_num
        else:
            return 0
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(456))
