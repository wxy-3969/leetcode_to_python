'''
给你两个字符串 haystack 和 needle
请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果 needle 不是 haystack 的一部分，则返回  -1 。
'''



class Solution:
    def strStr(self, haystack, needle):
        haystack_length = len(haystack)    # 获取字符串长度
        needle_length = len(needle)
        if needle_length == 0:
            return 0
        for i in range(haystack_length - needle_length + 1):
            if haystack[i:i + needle_length] == needle:    # 比较两个字符串是否相等
                return i
        return -1
# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.strStr("hello", "ll"))