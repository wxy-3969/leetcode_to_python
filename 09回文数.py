class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x!= 0):     # 如果x小于0或者x是10的倍数且不等于0，则不是回文数
            return False
        if x < 10:
            return True
        reversed_num = 0    # 反转后的数字
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10     # 将x的最后一位数字加到reversed_num的末尾
            x = x // 10
        return x == reversed_num or (x == reversed_num // 10 and x > 0)
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(131))