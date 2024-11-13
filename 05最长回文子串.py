'''
给你一个字符串 s,找到 s 中最长的 回文子串
'''
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        def expand_around_center(left, right):
            # 从中心向两边扩展，返回可以扩展的长度
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        start = 0  # 最长回文子串的起始位置
        end = 0    # 最长回文子串的结束位置
        for i in range(len(s)):
            # 以单个字符为中心
            len1 = expand_around_center(i, i)
            # 以两个字符之间的空隙为中心
            len2 = expand_around_center(i, i + 1)
            # 取最大长度
            max_len = max(len1, len2)
            # 如果找到更长的回文子串，更新起始和结束位置
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
# 测试代码
if __name__ == "__main__":
    test = "monmonmno"
    solution = Solution()
    result = solution.longestPalindrome(test)
    print(result)
