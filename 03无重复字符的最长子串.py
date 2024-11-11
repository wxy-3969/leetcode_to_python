'''
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。
 '''
 
class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:    # 如果字符串为空，直接返回0
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):    # 遍历字符串，i表示当前字符的索引
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])    # 从左边开始移除重复的字符
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len    # 更新最大长度
            lookup.add(s[i])
        return max_len
# 测试用例
if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
